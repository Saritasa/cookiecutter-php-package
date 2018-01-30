# PHP Package template

Template for PHP Packages, that can be installed with [Composer](https://getcomposer.org)

Includes pre-configured:
* [PHP_CodeSniffer](https://github.com/squizlabs/PHP_CodeSniffer) code style validator
* [PHPUnit](https://phpunit.de) unit tests
* [Travis CI](https://travis-ci.org) config to run **PHP_CodeSniffer** and **PHPUnit** and submit code coverage results to [codecov.io](https://codecov.io)
* README and version CHANGES templates
* .gitignore

## Usage

1. Install Cookiecutter, using

    ```bash
    $ pip install --user cookiecutter
    ```
   or any other method, described in [Cookiecutter Intallation](https://cookiecutter.readthedocs.io/en/latest/installation.html) Manual.
2. Create new project, using this template:

    ```bash
    $ cookiecutter gh:saritasa/cookiecutter-php-package
    ```
