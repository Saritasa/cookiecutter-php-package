<?php

namespace {{ cookiecutter.classes_namespace }}\Tests;

use PHPUnit\Framework\TestCase;

/**
 * Check that unit tests configured and can be run.
 */
class DemoTest extends TestCase
{
    /**
     * Simple test to check that unit tests working.
     */
    public function testUnitTestAvailable()
    {
        $this->assertTrue(true);
    }

    /**
     * Check, that main project class can is accessible in tests, using autoload
     */
    public function testExample()
    {
        $example = new \{{ cookiecutter.classes_namespace }}\Example();
        $this->assertEquals('test', $example->echoPhrase('test'));
    }
}
