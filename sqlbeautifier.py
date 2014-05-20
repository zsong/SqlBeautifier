import sublime, sublime_plugin

import sys
import os

sys.path.append(os.path.dirname(__file__))

if sys.version_info >= (3, 0):
    import sqlparse3 as sqlparse
else:
    import sqlparse2 as sqlparse


def plugin_loaded():
    global settings
    settings = sublime.load_settings('SQL Beautifier.sublime-settings')


class SqlBeautifierCommand(sublime_plugin.TextCommand):
    def format_sql(self, raw_sql):
        try:
            return sqlparse.format(raw_sql, 
                keyword_case=settings.get("keyword_case"),
                identifier_case=settings.get("identifier_case"),
                strip_comments=settings.get("strip_comments"),
                indent_tabs=settings.get("indent_tabs"),
                indent_width=settings.get("indent_width"),
                reindent=settings.get("reindent") 
            )
        except Exception as e:
            print(e)
            return None

    def run(self, edit):
        for region in self.view.sel():
            if not region.empty():
                selected_text = self.view.substr(region)
                
                foramtted_text = self.format_sql(selected_text)

                if foramtted_text:
                    self.view.replace(edit, region, foramtted_text)
                    self.view.set_syntax_file("Packages/SQL/SQL.tmLanguage")