# Project: ZX emulator of cassette
# File: Makefile
# Version: 0.1
# Create by: Rom1 <rom1@canel.ch> - CANEL - https://www.canel.ch
# Date: 28/08/2018
# Licence: GNU GENERAL PUBLIC LICENSE v3


NAME = zxemuk7
BIN_PATH = $(HOME)/bin
LOCAL_PATH = $(HOME)/local/$(NAME)

all: install

install: $(NAME).py
	cp $< $(BIN_PATH)/$(NAME)
	sed -ri 's!^local_path =.*$$!local_path = "$(LOCAL_PATH)"!' \
		$(BIN_PATH)/$(NAME)
	mkdir -p $(LOCAL_PATH)
	cp -r ./img $(LOCAL_PATH)

reinstall: desinst install

desinst:
	rm $(BIN_PATH)/$(NAME)
	rm -fr $(LOCAL_PATH)/img

mrproper: desint
	rm -fr $(LOCAL_PATH)
