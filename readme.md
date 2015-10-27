jenkins python demo
====================
演示python 项目如何用jenkins做持续集成

setup
----

```bash
virutalenv demo

source demo/bin/active

pip install -r requirements

./runtest.sh

python app.py
```


demo travis status: [![Build Status](https://travis-ci.org/oliveagle/jenkins_python_demo.svg?branch=master)](https://travis-ci.org/oliveagle/jenkins_python_demo)



dependencies
------------

mock dependencies are not fully managed by some pip version. so have to do it yourself. 


```bash
pip install pbr
pip install funcsigs
pip install mock

```
