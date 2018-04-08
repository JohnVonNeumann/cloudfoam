# Cloudfoam
Like many things, sometimes we become useful enough to know how to use something, but we may forget the little things. This is a repository which just has basic resource's templated with their possible values. It's not meant to be expansive, simply to provide a reference implementation template for those who work heavily with CF.

It's basically scooping the foam from the top.

## How to read the templates:

#### Conditionals
* Some attributes/resources have conditional elements, for example, `AWS::S3::Bucket::LifecycleConfiguration::Rules` requires that `one of more` of the attributes have been selected. In these instances, you will see comments such as:

        # COND => 1

* Which indicates that inside the attribute block, you must follow the `n rule` given, and select `n` of the attributes for CF to accept your template as valid.

#### Data Types
* Type is not listed as String if the input is limited to a range of choices, for example, in `AWS::S3::Bucket`, AccessControl can only be one of a finite selection, therefore, it is not listed as a `String Type` because the user does not have full control. If you see `(String)` listed on a resource attribute, you can safely assume that you as a user have full control over the input.

* Much like the above situation, you will find `ARNString` throughout the templates, I have included this when the `String` can only be accepted when it is in the form of an `AmazonResourceNumber`, hopefully providing more of a separation between what you have control over, and what you don't.

* `FileString` - When dealing with a `String` that must be supplied in the form of a file, eg: `index.html` the `Type` provided is `FileString`.

* `HostString` - When dealing with a `String` that must be supplied in the form of a hostname, eg: `sjhdqdjwqnd.randomregion.amazonaws.com` the `Type` provided is `HostString`.

## Contributing
* See an error? Feel free to create a PR!
* Been working on a module recently and see it's not here? Feel free to create a PR!
* Want to add something? Feel free to create a PR!
* Have an issue? Ticket it up!

## Gotchas when writing YAML
* I've been caught out numerous times by syntaxing of `List` and `StringList | List of Strings` due to the fact that some resources and attributes require individual items and some required lists that are nested. For example, I've had moments where I've just used:

        - List
          And Continuing

* And the second item hasn't been recognised, because you've created a `List`, not a list of lists. Which is what some things calls for. It all depends on the resource being called, which is why the Docs are always important.

#### All resources have their original source linked to them inside the templates themselves, all content belong to their original authors. I'm merely trying to amalgamate the information in one place for people to easily consult it.


## Codebase

### Installing modules

        pipenv install

### Running cli tool

        python cloudfoam.py AWS::EXAMPLE::Exampnet.yaml ~/code/cloudfoam/example.yaml

### Running tests

        pytest test/
