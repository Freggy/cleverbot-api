FROM fnndsc/ubuntu-python3

WORKDIR /lol
COPY . .
RUN apt update 
RUN apt install curl -y
RUN curl -fsSL https://deb.nodesource.com/setup_14.x | bash -
RUN apt-get install -y nodejs

RUN pip install cleverbotfree
RUN pip install flask
RUN playwright install firefox
RUN pip install -r requirements.txt

RUN apt-get install -y libgtk-3-0\
          libx11-6\
          libx11-xcb1\
          libxcb1\
          libxcomposite1\
          libxcursor1\
          libxdamage1\
          libxext6\
          libxfixes3\
          libxi6\
          libxrender1\
          libfreetype6\
          libfontconfig1\
          libdbus-glib-1-2\
          libdbus-1-3\
          libglib2.0-0\
          libpangocairo-1.0-0\
          libpango-1.0-0\
          libharfbuzz0b\
          libatk1.0-0\
          libcairo-gobject2\
          libcairo2\
          libgdk-pixbuf2.0-0\
          libxcb-shm0\
          libpangoft2-1.0-0\
          libxt6


CMD ["python" "api_new.py"]
