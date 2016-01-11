import sublime, sublime_plugin

import sys
import os

sys.path.append(os.path.dirname(__file__))

if sys.version_info >= (3, 0):
    import sqlparse3 as sqlparse
else:
    import sqlparse2 as sqlparse


# for ST2
settings = sublime.load_settings('SQL Beautifier.sublime-settings')

# for ST3
def plugin_loaded():
    global settings
    settings = sublime.load_settings('SQL Beautifier.sublime-settings')


class SqlBeautifierCommand(sublime_plugin.TextCommand):
    def format_sql(self, raw_sql):
        try:
            formatted_sql = sqlparse.format(raw_sql,
                keyword_case=settings.get("keyword_case"),
                identifier_case=settings.get("identifier_case"),
                strip_comments=settings.get("strip_comments"),
                indent_tabs=settings.get("indent_tabs"),
                indent_width=settings.get("indent_width"),
                reindent=settings.get("reindent")
            )

            if self.view.settings().get('ensure_newline_at_eof_on_save'):
                formatted_sql += "\n"

            return formatted_sql
        except Exception as e:
            print(e)
            return None

    def replace_region_with_formatted_sql(self, edit, region):
        selected_text = self.view.substr(region)
        foramtted_text = self.format_sql(selected_text)
        self.view.replace(edit, region, foramtted_text)

    def run(self, edit):
        window = self.view.window()
        view = window.active_view()

        for region in self.view.sel():
            if region.empty():
                selection = sublime.Region(0, self.view.size())
                self.replace_region_with_formatted_sql(edit, selection)
                self.view.set_syntax_file("Packages/SQL/SQL.tmLanguage")
            else:
                self.replace_region_with_formatted_sql(edit, region)