### ACCESS FIREFOX BOOKMARKS FROM COMMAND LINE

- This script can be used to open a url at a time, from an index 
  list of urls. 

- This script works under Linux.

- Linux less command used for paginating and searching in bookmark   list

- Export your own bookmarks.html file into application directory and run the application.


## How to run this app
- To run this app as a docker container:

  - Replace 'bmzi' in Dockerfile to your current username and build the docker image by:

    ```
    docker build -t bookmarkstarter .
    ```
  - Start the app by running docker with following command:

    ```
    $ docker run -e DISPLAY -v $HOME/.Xauthority:/home/<YOUR USERNAME>/.Xauthority --net=host -it bookmarkstarter:latest
    ```

