BIN_DIR = ~/bin
SRC_SCRIPT = memoru.py
DST_SCRIPT = $(BIN_DIR)/memoru

.PHONY: install clean

all:
	@echo "If you want to install this script, run 'make install'."

install: $(SRC_SCRIPT) $(BIN_DIR)
	cp -p $(SRC_SCRIPT) $(DST_SCRIPT)
	chmod +x $(DST_SCRIPT)

$(BIN_DIR):
	mkdir -p $(BIN_DIR)

clean:
ifneq (, $(wildcard $(DST_SCRIPT)))
	rm $(DST_SCRIPT)
endif

