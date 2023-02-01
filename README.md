## What's This?

This is a little package that will help you build a (currently only Python3.8) Lambda Layer out of any singular Python dependancy, ready for upload and deployment.

## Pre-requisites

Make sure you have Docker & Python installed! Run main as admin.

## What Hole Does it Fill?

So with Python dependencies, all dependencies have to be compiled on the target OS, and using the target Runtime. With the target OS being Amazon Linux, and all Lambda Layer creation documentation coming from the viewpoint that you are already on some instance that is running Amazon Linux/Linux, if you are working from Windows/Mac OS you can be left pretty in the dark - In this case you're going to need to follow one of the many much more tedious third-party web blog posts on how to use Docker, Makefiles, EC2 or WSL to do this. Beyond this, if targetting multiple Runtimes, you'll also have to setup a vitual enviroment for each in order to compile it's dependencies, before correctly structuring the dependencies for each Runtime before finally zipping your output file. (And maybe even later auto-uploading to AWS.)

This package works by using Docker to create a container running Amazon Linux with Python on your targetted Runtime, downloads the specified dependancies data into the container in an optimised structure expected by AWS Lambda, zips the file in the container, copies the .zip from the container to a specified location on your local machine, and removes the container when done. It supports any runtime, custom packages and even installing from links to private github repos - And you only have to use a single command to do all of it!

## To Come

Experiment with Docker in Docker - Use a single container to manage the creation of a number of nested containers that each target a different specified runtime.

