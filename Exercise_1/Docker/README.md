There is Dockerfile and python script to build container

Workarround to put output to /dev/null.

I wan't able to do so inside Docker container

* Workaround:
>sudo docker run --rm -e OPENWEATHER_API_KEY="<API_KEY from WEB>" -e CITY_NAME="Honolulu" weather:dev >/dev/null
