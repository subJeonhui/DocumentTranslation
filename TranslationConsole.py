from FileManagement.FileManager import *
from TranslationModel.TranslationModel import *
from TranslationConsoleConfiguration import *
import re
import os
from functools import reduce


class TranslateConsole:
    programFilePath = 'program.json'

    def __init__(self):
        self.__setProgramFile()
        self.fileManager = FileManager()
        today_logs = self.fileManager.read_log_with_date(self.logFilePath)
        self.count = reduce(lambda x, y: x + int(y[2]), today_logs, 0)
        self.translationModel = TranslationModel(self.envFilePath)
        self.translateText = ''

    def __setProgramFile(self):
        with open(self.programFilePath, 'r') as f:
            programFile = json.load(f)
            if programFile['env'] is None or programFile['log'] is None:
                raise Exception("The program file is wrong.")
            if not os.path.isfile(programFile['env']):
                raise Exception("env file path is wrong.")
            if not os.path.isfile(programFile['env']):
                raise Exception("Log file path is wrong.")
            self.max_count = 10000 if programFile['max'] is None else int(programFile['max'])
            self.envFilePath = programFile['env']
            self.logFilePath = programFile['log']

    def __file_tree(self, option=False):
        return TranslationConsoleConfiguration.show_tree(self.fileManager.root.show_tree(option=option), option=option)

    def __status(self):
        return TranslationConsoleConfiguration.show_status(self.fileManager.select,
                                                           self.translationModel.source,
                                                           self.translationModel.target,
                                                           self.count,
                                                           self.max_count)

    def select(self, path):
        self.fileManager.selectFilePath(path)

    def translate(self, show=True):
        text = self.fileManager.load()
        translateText = ''
        size = len(text)
        translated_text_count = 0
        if show:
            print()
            self.printProgressBar(0, size, length=50)
        for (idx, (state, line)) in enumerate(text):
            if state:
                # translateText += self.translationModel.translate(line)
                translateText += line  # testing
                translated_text_count += len(line)
            else:
                translateText += line
            if show:
                self.printProgressBar(idx + 1, size, length=50)
        self.fileManager.logging(self.logFilePath, translated_text_count)
        self.translateText = translateText

    def save(self, path):
        self.fileManager.save(path, self.translateText)

    def __c_select(self, path, hp=False):
        if hp:
            print(TranslationConsoleConfiguration.select_help)
            return
        if path is None:
            print(TranslationConsoleConfiguration.Error.the_number_of_argument_does_not_match.message())
        else:
            if os.path.isfile(path):
                self.select(path)
            else:
                print(TranslationConsoleConfiguration.Error.file_does_not_exist.message())

    def __c_translate(self, hp=False):
        if hp:
            print(TranslationConsoleConfiguration.translate_help)
            return
        if self.fileManager.select is None:
            print(TranslationConsoleConfiguration.Error.must_select_a_file.message())
        else:
            self.translate()

    def __c_save(self, path, hp=False):
        if hp:
            print(TranslationConsoleConfiguration.save_help)
            return
        if self.fileManager.select is None:
            print(TranslationConsoleConfiguration.Error.must_select_a_file.message())
        else:
            self.save(path)

    def __c_show(self, option, hp=False):
        if hp:
            print(TranslationConsoleConfiguration.show_help)
            return
        al = option in ['-al']
        print(self.__file_tree(al))

    def __c_help(self):
        print(TranslationConsoleConfiguration.help)

    def __c_set_target(self, lang_code, hp=False):
        if hp:
            print(TranslationConsoleConfiguration.setTarget_help)
            return
        if lang_code is None:
            print(TranslationConsoleConfiguration.Error.the_number_of_argument_does_not_match.message())
        elif lang_code not in TranslationConsoleConfiguration.support_language.values():
            print(TranslationConsoleConfiguration.Error.unsupported_language.message())
        else:
            self.translationModel.setTarget(lang_code)

    def __c_set_source(self, lang_code, hp=False):
        if hp:
            print(TranslationConsoleConfiguration.setSource_help)
            return
        if lang_code is None:
            print(TranslationConsoleConfiguration.Error.the_number_of_argument_does_not_match.message())
        elif lang_code not in TranslationConsoleConfiguration.support_language.values():
            print(TranslationConsoleConfiguration.Error.unsupported_language.message())
            print(TranslationConsoleConfiguration.support_language_description)
        else:
            self.translationModel.setSource(lang_code)

    def __c_status(self, hp=False):
        if hp:
            print(TranslationConsoleConfiguration.status_help)
            return
        print(self.__status())

    def __c_invalid_command(self):
        print(TranslationConsoleConfiguration.Error.invalid_command.message())
        print(TranslationConsoleConfiguration.help)

    def __c_quick_translate(self, path, path2, hp=False):
        if hp:
            print(TranslationConsoleConfiguration.quick_translate_help)
            return
        self.__c_select(path)
        if path is None: return
        self.__c_translate()
        self.__c_save(path2)

    def console(self):
        print(TranslationConsoleConfiguration.description + '\n')
        while True:
            selectFile = self.fileManager.select
            input_desc = " ► command: " if selectFile is None else f" ► ({selectFile.name}) command: "
            command = list(map(lambda x: x.lower(), re.sub(r' +', ' ', input(input_desc).strip()).split()))
            for i in range(3 - len(command)):
                command.append(None)
            hp = command[1] in ['-h', '-help']
            if command[0] in ['select', 's']:
                self.__c_select(command[1], hp=hp)
            elif command[0] in ['translate', 't']:
                self.__c_translate(hp=hp)
            elif command[0] in ['save', 'sv']:
                self.__c_save(command[1], hp=hp)
            elif command[0] in ['quicktranslate', 'qt']:
                self.__c_quick_translate(command[1], command[2], hp=hp)
            elif command[0] in ['show', 'sh']:
                self.__c_show(command[1], hp=hp)
            elif command[0] in ['settarget', 'st']:
                self.__c_set_target(command[1], hp=hp)
            elif command[0] in ['setsource', 'sc']:
                self.__c_set_source(command[1], hp=hp)
            elif command[0] in ['status', 'stat']:
                self.__c_status(hp=hp)
            elif command[0] in ['help', 'h']:
                self.__c_help()
            elif command[0] in ['close', 'c']:
                break
            else:
                self.__c_invalid_command()
        self.app.exec_()

    @staticmethod
    def printProgressBar(idx, total, length=100):
        percent = "{0:.1f}".format(100 * (idx / float(total)))
        filledLength = int(length * idx // total)
        bar = '█' * filledLength + '-' * (length - filledLength)
        print(f'\rtranslate |{bar}| {percent}% complete', end="\r")
        if idx == total:
            print('\n')


TranslateConsole().console()
