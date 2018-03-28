# Cloudfoam
Like many things, sometimes we become useful enough to know how to use something, but we may forget the little things. This is a repository which just has basic resource's templated with their possible values. It's not meant to be expansive, simply to provide a reference implementation template for those who work heavily with CF.

It's basically scooping the foam from the top.

## How to read the templates:
* Type is not listed as String if the input is limited to a range of choices, for example, in `AWS::S3::Bucket`, AccessControl can only be one of a finite selection, therefore, it is not listed as a `String Type` because the user does not have full control. If you see `(String)` listed on a resource attribute, you can safely assume that you as a user have full control over the input.

## Contributing
* See an error? Feel free to create a PR! 
* Been working on a module recently and see it's not here? Feel free to create a PR!
* Want to add something? Feel free to create a PR!
* Have an issue? Ticket it up!

#### All resources have their original source linked to them inside the templates themselves, all content belong to their original authors. I'm merely trying to amalgamate the information in one place for people to easily consult it.
