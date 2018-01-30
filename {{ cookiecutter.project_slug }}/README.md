# {{ cookiecutter.project_name }}

[![Build Status](https://travis-ci.org/{{ cookiecutter.repo_id }}.svg?branch=master)](https://travis-ci.org/{{ cookiecutter.repo_id }})
[![CodeCov](https://codecov.io/gh/{{ cookiecutter.repo_id }}/branch/master/graph/badge.svg)](https://codecov.io/gh/{{ cookiecutter.repo_id }})
[![Release](https://img.shields.io/github/release/{{ cookiecutter.repo_id }}.svg)](https://github.com/{{ cookiecutter.repo_id }}/releases)
[![PHPv](https://img.shields.io/packagist/php-v/{{ cookiecutter.package_name }}.svg)](http://www.php.net)
[![Downloads](https://img.shields.io/packagist/dt/{{ cookiecutter.package_name }}.svg)](https://packagist.org/packages/{{ cookiecutter.package_name }})

TODO: Project description

## Usage

Install the ```{{ cookiecutter.package_name }}``` package:

```bash
$ composer require {{ cookiecutter.package_name }}
```


## Contributing

1. Create fork, checkout it
2. Develop locally as usual. **Code must follow [PSR-1](http://www.php-fig.org/psr/psr-1/), [PSR-2](http://www.php-fig.org/psr/psr-2/)** -
    run [PHP_CodeSniffer](https://github.com/squizlabs/PHP_CodeSniffer) to ensure, that code follows style guides
3. **Cover added functionality with unit tests** and run [PHPUnit](https://phpunit.de/) to make sure, that all tests pass
4. Update [README.md](README.md) to describe new or changed functionality.
5. Add changes description to [CHANGES.md](CHANGES.md) file. Use [Semantic Versioning](https://semver.org/) convention to determine next version number.
6. When ready, create pull request

### Make shortcuts

If you have [GNU Make](https://www.gnu.org/software/make/) installed, you can use following shortcuts:

* ```make cs``` (instead of ```php vendor/bin/phpcs```) -
    run static code analysis with [PHP_CodeSniffer](https://github.com/squizlabs/PHP_CodeSniffer)
    to check code style
* ```make csfix``` (instead of ```php vendor/bin/phpcbf```) -
    fix code style violations with [PHP_CodeSniffer](https://github.com/squizlabs/PHP_CodeSniffer)
    automatically, where possible (ex. PSR-2 code formatting violations)
* ```make test``` (instead of ```php vendor/bin/phpunit```) -
    run tests with [PHPUnit](https://phpunit.de/)
* ```make install``` - instead of ```composer install```
* ```make all``` or just ```make``` without parameters -
    invokes described above **install**, **cs**, **test** tasks sequentially -
    project will be assembled, checked with linter and tested with one single command

## Resources

* [Bug Tracker]({{ cookiecutter.repo_url }}/issues)
* [Code]({{ cookiecutter.repo_url }})
* [Changes History](CHANGES.md)
* [Authors]({{ cookiecutter.repo_url }}/contributors)
