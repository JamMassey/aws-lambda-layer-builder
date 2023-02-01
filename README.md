## What's This?

This is a little package that will help you build a Lambda Layer out of any singular Python dependancy, ready for upload and deployment.

## Pre-requisites

Make sure you have Docker & Python installed! Run main as admin.

## What Hole Does it Fill?
Python dependencies for Lambda Layers all dependencies have to be compiled on the target OS and using the target runtime. This can mean that creating/updating Lambda Layers can be a tedious and tricky process if working on an OS that isn't Linux.

This package works by using Docker to create a container running Amazon Linux with Python on your targetted runtime, downloads the specified dependancies data into the container in an optimised structure expected by AWS Lambda, zips the file in the container, copies the .zip from the container to a specified location on your local machine, and removes the container when done. It supports any runtime, custom packages and even installing from links to private github repos - And you only have to use a single function to do all of it!

## To Come
Please feel free to make requests in issues!

 - Targetting multiple runtimes with a single layer.


