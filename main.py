# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring


from src.jrti import JRTI

jrti = JRTI()
jrti.run("scripts/hello-world.jrti")
