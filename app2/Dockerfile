FROM rust:1.67-slim-buster


WORKDIR /webapp

COPY Cargo.toml /webapp
COPY src/* /webapp/src/

RUN cargo build

EXPOSE 8001

ENTRYPOINT [ "cargo" ]

CMD [ "run" ]

