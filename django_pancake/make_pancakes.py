from flatten import flatten, TemplateDirectories
import os
import codecs

def make_pancakes(template_dirs, output_dir):
    templates = TemplateDirectories(template_dirs)
    for template_name in set(templates.list()):
        outfile = os.path.join(output_dir, template_name)
        print "'%s' -> '%s'" % (template_name, outfile)
        pancake = flatten(template_name, templates)
        try:
            os.makedirs(os.path.dirname(outfile))
        except OSError: # Already exists.
            pass
        with codecs.open(outfile, 'w', 'utf-8') as fp:
            fp.write(pancake)

if __name__ == "__main__":
    import sys
    make_pancakes(sys.argv[1:-1], sys.argv[-1])
