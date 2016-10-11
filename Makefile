TIKA_JAR := tika-server-1.13.jar

.PHONY: help
help: $(TIKA_JAR)
	java -jar $(TIKA_JAR) --help

$(TIKA_JAR):
	wget http://ftp.halifax.rwth-aachen.de/apache/tika/$(TIKA_JAR)

# Tika Usage
# ==========
# usage: tikaserver
#  -?,--help                      this help message
#  -C,--cors <arg>                origin allowed to make CORS requests
#                                 (default=NONE)
#                                 all allowed if "all"
#  -c,--config <arg>              Tika Configuration file to override
#                                 default config with.
#  -d,--digest <arg>              include digest in metadata, e.g.
#                                 md5,sha256
#  -dml,--digestMarkLimit <arg>   max number of bytes to mark on stream for
#                                 digest
#  -h,--host <arg>                host name (default = localhost, use * for
#                                 all)
#  -l,--log <arg>                 request URI log level ('debug' or 'info')
#  -p,--port <arg>                listen port (default = 9998)
#  -s,--includeStack              whether or not to return a stack trace
#                                 if there is an exception during 'parse'
