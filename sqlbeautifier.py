import sublime, sublime_plugin

try:
    #python 3
    from . import sqlparse
except (ValueError):
    #python 2
    import sqlparse

class SqlBeautifierCommand(sublime_plugin.TextCommand):
    def normalize_line_endings(self, string):
        string = string.replace('\r\n', '\n').replace('\r', '\n')
        line_endings = self.view.settings().get('default_line_ending')
        if line_endings == 'windows':
            string = string.replace('\n', '\r\n')
        elif line_endings == 'mac':
            string = string.replace('\n', '\r')
        return string

    def format_sql(self, raw_sql):
        try:
            return sqlparse.format(raw_sql, reindent=True, keyword_case='upper')
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