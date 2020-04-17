# kerberos-rest-api
REST interface for Kerberos' kadmin

This is a REST interface for Kerberos, based on the docs in [web.mit.edu](https://web.mit.edu/kerberos/krb5-1.12/doc/admin/admin_commands/kadmin_local.html).

## But why?

Why, do you ask? I answer: why not? But seriously, I just wanted to force myself to learn a little more about Kerberos.

## Installing

Be sure to add Kerberos' development libraries. In a Ubuntu/Debian system, 
installing the package `libkrb5-dev` does the trick.

Then, install the package using `pip` :

``` sh
$ pip install .
$ pip install -e '.[dev]'
```

