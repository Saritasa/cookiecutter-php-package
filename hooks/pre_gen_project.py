import re
import sys


MODULE_REGEX = r'^[a-zA-Z][-_a-zA-Z0-9]+$'
NAMESPACE_REGEX = r'^[a-zA-Z][\\_a-zA-Z0-9]+$'

module_name = '{{ cookiecutter.project_slug}}'

if not re.match(MODULE_REGEX, module_name):
    print('ERROR: The project slug (%s) is not a valid host name. Please use alphanumeric symobls or -' % module_name)

    #Exit to cancel project
    sys.exit(1)

namespace = '{{ cookiecutter.classes_namespace }}'

if not re.match(NAMESPACE_REGEX, namespace):
    print('ERROR: Root namespace (%s) is not a valid PHP namespace. Please use alphanumeric symobls or \\' % module_name)

    #Exit to cancel project
    sys.exit(1)
