import json
import jinja2

TEMPLATE_FILE = "template.html"


def render_html(**kwargs):
    templateLoader = jinja2.FileSystemLoader(searchpath="./")
    templateEnv = jinja2.Environment(loader=templateLoader)

    template = templateEnv.get_template(TEMPLATE_FILE)

    outputText = template.render(**kwargs)

    return outputText


def output_html_with_json(comments):
    HTML_file = open("live_doc.html", "w")
    HTML_file.write(render_html(comments=comments))
    HTML_file.close()


if __name__ == '__main__':
    with open('result_live.json') as f:
        comments = json.load(f)

    output_html_with_json(comments)