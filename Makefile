PROTO_DIR=src/proto
PROTO_FILE=$(PROTO_DIR)/greeter.proto
OUT_DIR_PY=src/infrastructure/grpc/protogen_py
OUT_DIR_GO=src/infrastructure/grpc/protogen_go

.PHONY: all clean proto-py proto-go protoc-gen-grpc-gateway
all: proto-py proto-go protoc-gen-grpc-gateway
clean:
	rm -rf $(OUT_DIR_PY)/*
	rm -rf $(OUT_DIR_GO)/*
		
proto-py:
	@mkdir -p $(OUT_DIR_PY)
	@python -m grpc_tools.protoc \
	-I $(PROTO_DIR) \
	--python_out=$(OUT_DIR_PY) \
	--grpc_python_out=$(OUT_DIR_PY) \
	$(PROTO_FILE)

proto-go:
	@mkdir -p $(OUT_DIR_GO)
	@protoc -I $(PROTO_DIR) \
		--go_out=$(OUT_DIR_GO) \
		--go_opt=paths=source_relative \
		--go-grpc_out=$(OUT_DIR_GO) \
		--go-grpc_opt=paths=source_relative \
		$(PROTO_FILE)

protoc-gen-grpc-gateway:
	@mkdir -p $(OUT_DIR_GO)
	@protoc -I $(PROTO_DIR) \
		--grpc-gateway_out=$(OUT_DIR_GO) \
		--grpc-gateway_opt=paths=source_relative \
		--grpc-gateway_opt=generate_unbound_methods=true \
		$(PROTO_FILE)

up:
	docker compose up -d
down:
	docker compose down
logs:
	docker compose logs -f -n 100
