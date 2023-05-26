import re
from enum import Enum


class StrEnum(str, Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


class TranslationConsoleConfiguration:
    __default = "\033[0m"
    __black = "\033[90m"
    __red = "\033[91m"
    __green = "\033[92m"
    __yellow = "\033[93m"
    __blue = '\033[94m'
    __magenta = '\033[95m'
    __cyan = '\033[96m'

    description = ''.join(
        [f"{__yellow}⎧{'':⎺^80}⎫\n",
         f"{__yellow}|{__blue}" + "{:^80}".format(
             "     ______                                              _       ") + "\033[93m|\n",
         f"{__yellow}|{__blue}" + "{:^80}".format(
             "     |  _  \                                            | |      ") + "\033[93m|\n",
         f"{__yellow}|{__blue}" + "{:^80}".format(
             "     | | | |  ___    ___  _   _  _ __ ___    ___  _ __  | |_     ") + "\033[93m|\n",
         f"{__yellow}|{__blue}" + "{:^80}".format(
             "     | | | | / _ \  / __|| | | || '_ ` _ \  / _ \| '_ \ | __|    ") + "\033[93m|\n",
         f"{__yellow}|{__blue}" + "{:^80}".format(
             "     | |/ / | (_) || (__ | |_| || | | | | ||  __/| | | || |_     ") + "\033[93m|\n",
         f"{__yellow}|{__blue}" + "{:^80}".format(
             "     |___/   \___/  \___| \__,_||_| |_| |_| \___||_| |_| \__|    ") + "\033[93m|\n",
         f"{__yellow}|{__magenta}" + "{:^80}".format(
             " _____                           _         _    _                ") + "\033[93m|\n",
         f"{__yellow}|{__magenta}" + "{:^80}".format(
             "|_   _|                         | |       | |  (_)               ") + "\033[93m|\n",
         f"{__yellow}|{__magenta}" + "{:^80}".format(
             "  | |   _ __   __ _  _ __   ___ | |  __ _ | |_  _   ___   _ __   ") + "\033[93m|\n",
         f"{__yellow}|{__magenta}" + "{:^80}".format(
             "  | |  | '__| / _` || '_ \ / __|| | / _` || __|| | / _ \ | '_ \  ") + "\033[93m|\n",
         f"{__yellow}|{__magenta}" + "{:^80}".format(
             "  | |  | |   | (_| || | | |\__ \| || (_| || |_ | || (_) || | | | ") + "\033[93m|\n",
         f"{__yellow}|{__magenta}" + "{:^80}".format(
             "  \_/  |_|    \__,_||_| |_||___/|_| \__,_| \__||_| \___/ |_| |_| ") + "\033[93m|\n",
         f"{__yellow}|{__magenta}" + "{:^80}".format("") + __default + '\033[93m|\n',
         f"{__yellow}⎩{'':⎽^80}⎭" + __default])

    help = __cyan + f"\n⎧⎺⎺{' Document Translation Commands ':⎺<78}⎫\n" \
                    f"|{' select':16}|{' s':4} {'[path]':12}{': Select the file':46}|\n" \
                    f"|{' translate':16}|{' t':4} {'':12}{': Translate the selected file.':46}|\n" \
                    f"|{' save':16}|{' sv':4} {'(path)':12}{': Save the selected file.':46}|\n" \
                    f"|{' quickTranslate':16}|{' qt':4} {'[path](path)':12}{': select, translate, save':46}|\n" \
                    f"|{' show':16}|{' sh':4} {'(option)':12}{': Shows the structure of valid document files.':46}|\n" \
                    f"|{' setSource':16}|{' sc':4} {'[lang code]':12}{': Set the source language.':46}|\n" \
                    f"|{' setTarget':16}|{' st':4} {'[lang code]':12}{': Set the target language.':46}|\n" \
                    f"|{' status':16}|{' stat':17}{': Shows the current status.':46}|\n" \
                    f"|{' help':16}|{' h':4} {'':12}{': Shows the commands in Document Translation.':46}|\n" \
                    f"|{' close':16}|{' c':4} {'':12}{': Exit the program.':46}|\n" \
                    f"|{'':-<80}|\n" \
                    f"|{' You can translate document files in the following ways':80}|\n" \
                    f"|{' : select -> translate -> save':80}|\n" \
                    f"|{'':-<80}|\n" \
                    f"|{' (command) -h : You can check the detailed description of the command.':80}|\n" \
                    f"⎩{'':⎽^80}⎭{__default}\n"

    select_help = __cyan + f"\n⎧⎺⎺{' select ':⎺<78}⎫\n" \
                           f"|{' select':16}|{' s':4} {'[path]':12}{': Select the file':46}|\n" \
                           f"|{'':-^16}-{'':-^5}{'':-^12}{'':-^46}|\n" \
                           f"|{' [path]':16}{': The path to the file you want to select':64}|\n" \
                           f"⎩{'':⎽^80}⎭{__default}\n"

    translate_help = __cyan + f"\n⎧⎺⎺{' translate ':⎺<78}⎫\n" \
                              f"|{' translate':16}|{' t':4} {'':12}{': Translate the selected file.':46}|\n" \
                              f"⎩{'':⎽^80}⎭{__default}\n"

    save_help = __cyan + f"\n⎧⎺⎺{' save ':⎺<78}⎫\n" \
                         f"|{' save':16}|{' sv':4} {'(path)':12}{': Save the selected file.':46}|\n" \
                         f"|{'':-^16}-{'':-^5}{'':-^12}{'':-^46}|\n" \
                         f"|{' [path]':16}{': The path to the file you want to save':64}|\n" \
                         f"|{'':16}{'  If not entered, it is saved in the selected file location.':64}|\n" \
                         f"⎩{'':⎽^80}⎭{__default}\n"

    quick_translate_help = __cyan + f"\n⎧⎺⎺{' quick translate ':⎺<78}⎫\n" \
                                    f"|{' quickTranslate':16}|{' qt':4} {'[path](path)':12}{': select, translate, save':46}|\n" \
                                    f"|{'':-^16}-{'':-^5}{'':-^12}{'':-^46}|\n" \
                                    f"|{' [path]':16}{': The path to the file you want to select':64}|\n" \
                                    f"|{' (path)':16}{': The path to the file you want to save':64}|\n" \
                                    f"|{'':16}{'  If not entered, it is saved in the selected file location.':64}|\n" \
                                    f"⎩{'':⎽^80}⎭{__default}\n"

    show_help = __cyan + f"\n⎧⎺⎺{' show ':⎺<78}⎫\n" \
                         f"|{' show':16}|{' sh':4} {'(option)':12}{': Shows the structure of valid document files.':46}|\n" \
                         f"|{'':-^16}-{'':-^5}{'':-^12}{'':-^46}|\n" \
                         f"|{' (option)':16}{': Shows a tree of selectable files from the current path.':64}|\n" \
                         f"|{' (option) -al':16}{': Shows a tree of all the files from the current path.':64}|\n" \
                         f"⎩{'':⎽^80}⎭{__default}\n"

    setSource_help = __cyan + f"\n⎧⎺⎺{' set source ':⎺<78}⎫\n" \
                              f"|{' setSource':16}|{' sc':4} {'[lang code]':12}{': Set the source language.':46}|\n" \
                              f"|{'':-^16}-{'':-^5}{'':-^12}{'':-^46}|\n" \
                              f"|{' [lang code]':16}{': set language code of the file to be translated':64}|\n" \
                              f"⎩{'':⎽^80}⎭{__default}\n"

    setTarget_help = __cyan + f"\n⎧⎺⎺{' set target ':⎺<78}⎫\n" \
                              f"|{' setTarget':16}|{' st':4} {'[lang code]':12}{': Set the target language.':46}|\n" \
                              f"|{'':-^16}-{'':-^5}{'':-^12}{'':-^46}|\n" \
                              f"|{' [lang code]':16}{': The language code in which you want to translate the file':64}|\n" \
                              f"⎩{'':⎽^80}⎭{__default}\n"

    status_help = __cyan + f"\n⎧⎺⎺{' status ':⎺<78}⎫\n" \
                           f"|{' status':16}|{' stat':17}{': Shows the current status.':46}|\n" \
                           f"⎩{'':⎽^80}⎭{__default}\n"

    support_language = {'Korean': 'ko',
                        'English': 'en',
                        'Japanese': 'ja',
                        'Simplified Chinese': 'zh-cn',
                        'Traditional Chinese': 'zh-tw',
                        'Vietnamese': 'vi',
                        'Indonesian': 'id',
                        'Thai': 'th',
                        'German': 'de',
                        'Russian': 'ru',
                        'Spanish': 'es',
                        'Italian': 'it',
                        'French': 'fr'}

    support_language_description = __cyan + \
                                   f"⎧⎺⎺{' supported language ':⎺<38}⎫\n" \
                                   f"|{'language':^30} | {'code':^6} |\n" + \
                                   f"|{'':-^30} | {'':-^6} |\n" + \
                                   ''.join([f'|{key:^30} | {value:^6} |\n' for (key, value) in
                                            {'Korean': 'ko',
                                             'English': 'en',
                                             'Japanese': 'ja',
                                             'Simplified Chinese': 'zh-cn',
                                             'Traditional Chinese': 'zh-tw',
                                             'Vietnamese': 'vi',
                                             'Indonesian': 'id',
                                             'Thai': 'th',
                                             'German': 'de',
                                             'Russian': 'ru',
                                             'Spanish': 'es',
                                             'Italian': 'it',
                                             'French': 'fr'}.items()]) \
                                   + f"⎩{'':⎽^40}⎭{__default}\n"

    @staticmethod
    def show_tree(treeText, option=True):
        maxCount = max(list(map(lambda x: len(x) + 4, treeText.split('\n'))) + [80])
        color_text = []
        treeText = re.sub('\t', '    ', treeText)
        for text in treeText.split('\n'):
            stripText = text.strip()
            if len(stripText) >= 1:
                t = TranslationConsoleConfiguration.__cyan + "|"
                if stripText[0] == '➤':
                    t += TranslationConsoleConfiguration.__green
                elif stripText[0] == '▷':
                    t += TranslationConsoleConfiguration.__black
                else:
                    t += TranslationConsoleConfiguration.__yellow
                t += ("{:⎽<" + f"{maxCount}" + "}").format(text) + \
                     TranslationConsoleConfiguration.__cyan + '|\n' + \
                     TranslationConsoleConfiguration.__default
                color_text.append(t)

        return TranslationConsoleConfiguration.__cyan + \
            ("\n⎧⎺⎺{:⎺<" + f"{maxCount - 2}" + "}⎫\n").format(' Validation File Tree ' if option else ' File Tree ') + \
            "".join(color_text) + \
            TranslationConsoleConfiguration.__cyan + \
            ("⎩{:⎽^" + f"{maxCount}" + "}⎭").format('') + f"{TranslationConsoleConfiguration.__default}\n"

    @staticmethod
    def show_status(selectedFile, source, target, count, max_count):
        sourceLang = ''
        targetLang = ''
        for key, value in TranslationConsoleConfiguration.support_language.items():
            if value == source:
                sourceLang = key
            if value == target:
                targetLang = key

        percent = "{0:.1f}".format(100 * (count / float(max_count)))
        barColor = TranslationConsoleConfiguration.__green
        if 100 * (count / float(max_count)) >= 50.0:
            barColor = TranslationConsoleConfiguration.__yellow
        if 100 * (count / float(max_count)) >= 80.0:
            barColor = TranslationConsoleConfiguration.__red

        return TranslationConsoleConfiguration.__cyan + \
            f"\n⎧⎺⎺{' status ':⎺<78}⎫\n" + \
            f"|{'':-<80}|\n" + \
            f"|{' translate':^10} | " + \
            barColor + \
            "{:-<50}".format('█' * int(50 * min(count, max_count) // max_count)) + \
            TranslationConsoleConfiguration.__cyan + \
            " | {:^14}|\n".format(f"{percent}% filled") + \
            f"|{'':-<80}|\n" + \
            f"|{'source language':^20}" + "{:60}|\n".format(f": {targetLang} ({target})") + \
            f"|{'target language':^20}" + "{:60}|\n".format(f": {sourceLang} ({source})") + \
            f"|{'':-<80}|\n" + \
            f"|{'selected file':^20}" + "{:60}|\n".format(
                f": {selectedFile.fullPath().split('/')[-1] if selectedFile is not None else 'None'}") + \
            (f"|{'':^20}" + "{:60}|\n".format(f"  {selectedFile.fullPath()}") if selectedFile is not None else '') + \
            f"⎩{'':⎽^80}⎭{TranslationConsoleConfiguration.__default}\n"

    class Error(StrEnum):
        must_select_a_file = 'Must select a file.'
        the_number_of_argument_does_not_match = 'The number of argument does not match.'
        invalid_command = 'Invalid command.'
        file_does_not_exist = 'File does not exist.'
        unsupported_language = 'Unsupported language.'

        def message(self):
            return '\033[91m' + 'Error: ' + self.value + '\033[0m\n'
