CMD_PREFIX = "docker exec nodeosd cleos"
SYSTEM_ACCOUNTS = ['eosio.bpay',
'eosio.msig',
'eosio.names',
'eosio.ram',
'eosio.ramfee',
'eosio.saving',
'eosio.stake',
'eosio.vpay']
DOCKER_IMAGE = "johnnyzhao/eos:mainnet-1.0.6-unstake-in-5mins"
BIOS_DOCKER_COMPOSE = """
version: "3"

services:
  nodeosd:
    image: %s
    command: nodeosd.sh --data-dir /opt/eosio/bin/data-dir --genesis-json /opt/eosio/bin/data-dir/genesis.json --replay-blockchain
    hostname: nodeosd
    container_name: nodeosd
    ports:
      - 8888:8888
      - 9876:9876
    expose:
      - "9876"
    volumes:
      - /data/bios-node:/opt/eosio/bin/data-dir

""" % DOCKER_IMAGE
