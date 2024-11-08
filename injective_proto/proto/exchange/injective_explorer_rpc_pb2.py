from injective_proto.proto.descriptor import INJECTIVE_DESCRIPTOR_POOL
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: exchange/injective_explorer_rpc.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = INJECTIVE_DESCRIPTOR_POOL.AddSerializedFile(b'\n%exchange/injective_explorer_rpc.proto\x12\x16injective_explorer_rpc\"\xc4\x02\n\x14GetAccountTxsRequest\x12\x18\n\x07\x61\x64\x64ress\x18\x01 \x01(\tR\x07\x61\x64\x64ress\x12\x16\n\x06\x62\x65\x66ore\x18\x02 \x01(\x04R\x06\x62\x65\x66ore\x12\x14\n\x05\x61\x66ter\x18\x03 \x01(\x04R\x05\x61\x66ter\x12\x14\n\x05limit\x18\x04 \x01(\x11R\x05limit\x12\x12\n\x04skip\x18\x05 \x01(\x04R\x04skip\x12\x12\n\x04type\x18\x06 \x01(\tR\x04type\x12\x16\n\x06module\x18\x07 \x01(\tR\x06module\x12\x1f\n\x0b\x66rom_number\x18\x08 \x01(\x12R\nfromNumber\x12\x1b\n\tto_number\x18\t \x01(\x12R\x08toNumber\x12\x1d\n\nstart_time\x18\n \x01(\x12R\tstartTime\x12\x19\n\x08\x65nd_time\x18\x0b \x01(\x12R\x07\x65ndTime\x12\x16\n\x06status\x18\x0c \x01(\tR\x06status\"\x89\x01\n\x15GetAccountTxsResponse\x12\x36\n\x06paging\x18\x01 \x01(\x0b\x32\x1e.injective_explorer_rpc.PagingR\x06paging\x12\x38\n\x04\x64\x61ta\x18\x02 \x03(\x0b\x32$.injective_explorer_rpc.TxDetailDataR\x04\x64\x61ta\"\x86\x01\n\x06Paging\x12\x14\n\x05total\x18\x01 \x01(\x12R\x05total\x12\x12\n\x04\x66rom\x18\x02 \x01(\x11R\x04\x66rom\x12\x0e\n\x02to\x18\x03 \x01(\x11R\x02to\x12.\n\x13\x63ount_by_subaccount\x18\x04 \x01(\x12R\x11\x63ountBySubaccount\x12\x12\n\x04next\x18\x05 \x03(\tR\x04next\"\xab\x05\n\x0cTxDetailData\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12!\n\x0c\x62lock_number\x18\x02 \x01(\x04R\x0b\x62lockNumber\x12\'\n\x0f\x62lock_timestamp\x18\x03 \x01(\tR\x0e\x62lockTimestamp\x12\x12\n\x04hash\x18\x04 \x01(\tR\x04hash\x12\x12\n\x04\x63ode\x18\x05 \x01(\rR\x04\x63ode\x12\x12\n\x04\x64\x61ta\x18\x06 \x01(\x0cR\x04\x64\x61ta\x12\x12\n\x04info\x18\x08 \x01(\tR\x04info\x12\x1d\n\ngas_wanted\x18\t \x01(\x12R\tgasWanted\x12\x19\n\x08gas_used\x18\n \x01(\x12R\x07gasUsed\x12\x37\n\x07gas_fee\x18\x0b \x01(\x0b\x32\x1e.injective_explorer_rpc.GasFeeR\x06gasFee\x12\x1c\n\tcodespace\x18\x0c \x01(\tR\tcodespace\x12\x35\n\x06\x65vents\x18\r \x03(\x0b\x32\x1d.injective_explorer_rpc.EventR\x06\x65vents\x12\x17\n\x07tx_type\x18\x0e \x01(\tR\x06txType\x12\x1a\n\x08messages\x18\x0f \x01(\x0cR\x08messages\x12\x41\n\nsignatures\x18\x10 \x03(\x0b\x32!.injective_explorer_rpc.SignatureR\nsignatures\x12\x12\n\x04memo\x18\x11 \x01(\tR\x04memo\x12\x1b\n\ttx_number\x18\x12 \x01(\x04R\x08txNumber\x12\x30\n\x14\x62lock_unix_timestamp\x18\x13 \x01(\x04R\x12\x62lockUnixTimestamp\x12\x1b\n\terror_log\x18\x14 \x01(\tR\x08\x65rrorLog\x12\x12\n\x04logs\x18\x15 \x01(\x0cR\x04logs\x12\x1b\n\tclaim_ids\x18\x16 \x03(\x12R\x08\x63laimIds\"\x91\x01\n\x06GasFee\x12:\n\x06\x61mount\x18\x01 \x03(\x0b\x32\".injective_explorer_rpc.CosmosCoinR\x06\x61mount\x12\x1b\n\tgas_limit\x18\x02 \x01(\x04R\x08gasLimit\x12\x14\n\x05payer\x18\x03 \x01(\tR\x05payer\x12\x18\n\x07granter\x18\x04 \x01(\tR\x07granter\":\n\nCosmosCoin\x12\x14\n\x05\x64\x65nom\x18\x01 \x01(\tR\x05\x64\x65nom\x12\x16\n\x06\x61mount\x18\x02 \x01(\tR\x06\x61mount\"\xa9\x01\n\x05\x45vent\x12\x12\n\x04type\x18\x01 \x01(\tR\x04type\x12M\n\nattributes\x18\x02 \x03(\x0b\x32-.injective_explorer_rpc.Event.AttributesEntryR\nattributes\x1a=\n\x0f\x41ttributesEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"w\n\tSignature\x12\x16\n\x06pubkey\x18\x01 \x01(\tR\x06pubkey\x12\x18\n\x07\x61\x64\x64ress\x18\x02 \x01(\tR\x07\x61\x64\x64ress\x12\x1a\n\x08sequence\x18\x03 \x01(\x04R\x08sequence\x12\x1c\n\tsignature\x18\x04 \x01(\tR\tsignature\"\x99\x01\n\x15GetContractTxsRequest\x12\x18\n\x07\x61\x64\x64ress\x18\x01 \x01(\tR\x07\x61\x64\x64ress\x12\x14\n\x05limit\x18\x02 \x01(\x11R\x05limit\x12\x12\n\x04skip\x18\x03 \x01(\x04R\x04skip\x12\x1f\n\x0b\x66rom_number\x18\x04 \x01(\x12R\nfromNumber\x12\x1b\n\tto_number\x18\x05 \x01(\x12R\x08toNumber\"\x8a\x01\n\x16GetContractTxsResponse\x12\x36\n\x06paging\x18\x01 \x01(\x0b\x32\x1e.injective_explorer_rpc.PagingR\x06paging\x12\x38\n\x04\x64\x61ta\x18\x02 \x03(\x0b\x32$.injective_explorer_rpc.TxDetailDataR\x04\x64\x61ta\"\x9b\x01\n\x17GetContractTxsV2Request\x12\x18\n\x07\x61\x64\x64ress\x18\x01 \x01(\tR\x07\x61\x64\x64ress\x12\x16\n\x06height\x18\x02 \x01(\x04R\x06height\x12\x12\n\x04\x66rom\x18\x03 \x01(\x12R\x04\x66rom\x12\x0e\n\x02to\x18\x04 \x01(\x12R\x02to\x12\x14\n\x05limit\x18\x05 \x01(\x11R\x05limit\x12\x14\n\x05token\x18\x06 \x01(\tR\x05token\"h\n\x18GetContractTxsV2Response\x12\x12\n\x04next\x18\x01 \x03(\tR\x04next\x12\x38\n\x04\x64\x61ta\x18\x02 \x03(\x0b\x32$.injective_explorer_rpc.TxDetailDataR\x04\x64\x61ta\"z\n\x10GetBlocksRequest\x12\x16\n\x06\x62\x65\x66ore\x18\x01 \x01(\x04R\x06\x62\x65\x66ore\x12\x14\n\x05\x61\x66ter\x18\x02 \x01(\x04R\x05\x61\x66ter\x12\x14\n\x05limit\x18\x03 \x01(\x11R\x05limit\x12\x12\n\x04\x66rom\x18\x04 \x01(\x04R\x04\x66rom\x12\x0e\n\x02to\x18\x05 \x01(\x04R\x02to\"\x82\x01\n\x11GetBlocksResponse\x12\x36\n\x06paging\x18\x01 \x01(\x0b\x32\x1e.injective_explorer_rpc.PagingR\x06paging\x12\x35\n\x04\x64\x61ta\x18\x02 \x03(\x0b\x32!.injective_explorer_rpc.BlockInfoR\x04\x64\x61ta\"\xad\x02\n\tBlockInfo\x12\x16\n\x06height\x18\x01 \x01(\x04R\x06height\x12\x1a\n\x08proposer\x18\x02 \x01(\tR\x08proposer\x12\x18\n\x07moniker\x18\x03 \x01(\tR\x07moniker\x12\x1d\n\nblock_hash\x18\x04 \x01(\tR\tblockHash\x12\x1f\n\x0bparent_hash\x18\x05 \x01(\tR\nparentHash\x12&\n\x0fnum_pre_commits\x18\x06 \x01(\x12R\rnumPreCommits\x12\x17\n\x07num_txs\x18\x07 \x01(\x12R\x06numTxs\x12\x33\n\x03txs\x18\x08 \x03(\x0b\x32!.injective_explorer_rpc.TxDataRPCR\x03txs\x12\x1c\n\ttimestamp\x18\t \x01(\tR\ttimestamp\"\xa0\x02\n\tTxDataRPC\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12!\n\x0c\x62lock_number\x18\x02 \x01(\x04R\x0b\x62lockNumber\x12\'\n\x0f\x62lock_timestamp\x18\x03 \x01(\tR\x0e\x62lockTimestamp\x12\x12\n\x04hash\x18\x04 \x01(\tR\x04hash\x12\x1c\n\tcodespace\x18\x05 \x01(\tR\tcodespace\x12\x1a\n\x08messages\x18\x06 \x01(\tR\x08messages\x12\x1b\n\ttx_number\x18\x07 \x01(\x04R\x08txNumber\x12\x1b\n\terror_log\x18\x08 \x01(\tR\x08\x65rrorLog\x12\x12\n\x04\x63ode\x18\t \x01(\rR\x04\x63ode\x12\x1b\n\tclaim_ids\x18\n \x03(\x12R\x08\x63laimIds\"!\n\x0fGetBlockRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\"u\n\x10GetBlockResponse\x12\x0c\n\x01s\x18\x01 \x01(\tR\x01s\x12\x16\n\x06\x65rrmsg\x18\x02 \x01(\tR\x06\x65rrmsg\x12;\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32\'.injective_explorer_rpc.BlockDetailInfoR\x04\x64\x61ta\"\xcd\x02\n\x0f\x42lockDetailInfo\x12\x16\n\x06height\x18\x01 \x01(\x04R\x06height\x12\x1a\n\x08proposer\x18\x02 \x01(\tR\x08proposer\x12\x18\n\x07moniker\x18\x03 \x01(\tR\x07moniker\x12\x1d\n\nblock_hash\x18\x04 \x01(\tR\tblockHash\x12\x1f\n\x0bparent_hash\x18\x05 \x01(\tR\nparentHash\x12&\n\x0fnum_pre_commits\x18\x06 \x01(\x12R\rnumPreCommits\x12\x17\n\x07num_txs\x18\x07 \x01(\x12R\x06numTxs\x12\x1b\n\ttotal_txs\x18\x08 \x01(\x12R\x08totalTxs\x12\x30\n\x03txs\x18\t \x03(\x0b\x32\x1e.injective_explorer_rpc.TxDataR\x03txs\x12\x1c\n\ttimestamp\x18\n \x01(\tR\ttimestamp\"\xd3\x02\n\x06TxData\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12!\n\x0c\x62lock_number\x18\x02 \x01(\x04R\x0b\x62lockNumber\x12\'\n\x0f\x62lock_timestamp\x18\x03 \x01(\tR\x0e\x62lockTimestamp\x12\x12\n\x04hash\x18\x04 \x01(\tR\x04hash\x12\x1c\n\tcodespace\x18\x05 \x01(\tR\tcodespace\x12\x1a\n\x08messages\x18\x06 \x01(\x0cR\x08messages\x12\x1b\n\ttx_number\x18\x07 \x01(\x04R\x08txNumber\x12\x1b\n\terror_log\x18\x08 \x01(\tR\x08\x65rrorLog\x12\x12\n\x04\x63ode\x18\t \x01(\rR\x04\x63ode\x12 \n\x0ctx_msg_types\x18\n \x01(\x0cR\ntxMsgTypes\x12\x12\n\x04logs\x18\x0b \x01(\x0cR\x04logs\x12\x1b\n\tclaim_ids\x18\x0c \x03(\x12R\x08\x63laimIds\"\x16\n\x14GetValidatorsRequest\"t\n\x15GetValidatorsResponse\x12\x0c\n\x01s\x18\x01 \x01(\tR\x01s\x12\x16\n\x06\x65rrmsg\x18\x02 \x01(\tR\x06\x65rrmsg\x12\x35\n\x04\x64\x61ta\x18\x03 \x03(\x0b\x32!.injective_explorer_rpc.ValidatorR\x04\x64\x61ta\"\xb5\x07\n\tValidator\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x18\n\x07moniker\x18\x02 \x01(\tR\x07moniker\x12)\n\x10operator_address\x18\x03 \x01(\tR\x0foperatorAddress\x12+\n\x11\x63onsensus_address\x18\x04 \x01(\tR\x10\x63onsensusAddress\x12\x16\n\x06jailed\x18\x05 \x01(\x08R\x06jailed\x12\x16\n\x06status\x18\x06 \x01(\x11R\x06status\x12\x16\n\x06tokens\x18\x07 \x01(\tR\x06tokens\x12)\n\x10\x64\x65legator_shares\x18\x08 \x01(\tR\x0f\x64\x65legatorShares\x12N\n\x0b\x64\x65scription\x18\t \x01(\x0b\x32,.injective_explorer_rpc.ValidatorDescriptionR\x0b\x64\x65scription\x12)\n\x10unbonding_height\x18\n \x01(\x12R\x0funbondingHeight\x12%\n\x0eunbonding_time\x18\x0b \x01(\tR\runbondingTime\x12\'\n\x0f\x63ommission_rate\x18\x0c \x01(\tR\x0e\x63ommissionRate\x12.\n\x13\x63ommission_max_rate\x18\r \x01(\tR\x11\x63ommissionMaxRate\x12;\n\x1a\x63ommission_max_change_rate\x18\x0e \x01(\tR\x17\x63ommissionMaxChangeRate\x12\x34\n\x16\x63ommission_update_time\x18\x0f \x01(\tR\x14\x63ommissionUpdateTime\x12\x1a\n\x08proposed\x18\x10 \x01(\x04R\x08proposed\x12\x16\n\x06signed\x18\x11 \x01(\x04R\x06signed\x12\x16\n\x06missed\x18\x12 \x01(\x04R\x06missed\x12\x1c\n\ttimestamp\x18\x13 \x01(\tR\ttimestamp\x12\x41\n\x07uptimes\x18\x14 \x03(\x0b\x32\'.injective_explorer_rpc.ValidatorUptimeR\x07uptimes\x12N\n\x0fslashing_events\x18\x15 \x03(\x0b\x32%.injective_explorer_rpc.SlashingEventR\x0eslashingEvents\x12+\n\x11uptime_percentage\x18\x16 \x01(\x01R\x10uptimePercentage\x12\x1b\n\timage_url\x18\x17 \x01(\tR\x08imageUrl\"\xc8\x01\n\x14ValidatorDescription\x12\x18\n\x07moniker\x18\x01 \x01(\tR\x07moniker\x12\x1a\n\x08identity\x18\x02 \x01(\tR\x08identity\x12\x18\n\x07website\x18\x03 \x01(\tR\x07website\x12)\n\x10security_contact\x18\x04 \x01(\tR\x0fsecurityContact\x12\x18\n\x07\x64\x65tails\x18\x05 \x01(\tR\x07\x64\x65tails\x12\x1b\n\timage_url\x18\x06 \x01(\tR\x08imageUrl\"L\n\x0fValidatorUptime\x12!\n\x0c\x62lock_number\x18\x01 \x01(\x04R\x0b\x62lockNumber\x12\x16\n\x06status\x18\x02 \x01(\tR\x06status\"\xe0\x01\n\rSlashingEvent\x12!\n\x0c\x62lock_number\x18\x01 \x01(\x04R\x0b\x62lockNumber\x12\'\n\x0f\x62lock_timestamp\x18\x02 \x01(\tR\x0e\x62lockTimestamp\x12\x18\n\x07\x61\x64\x64ress\x18\x03 \x01(\tR\x07\x61\x64\x64ress\x12\x14\n\x05power\x18\x04 \x01(\x04R\x05power\x12\x16\n\x06reason\x18\x05 \x01(\tR\x06reason\x12\x16\n\x06jailed\x18\x06 \x01(\tR\x06jailed\x12#\n\rmissed_blocks\x18\x07 \x01(\x04R\x0cmissedBlocks\"/\n\x13GetValidatorRequest\x12\x18\n\x07\x61\x64\x64ress\x18\x01 \x01(\tR\x07\x61\x64\x64ress\"s\n\x14GetValidatorResponse\x12\x0c\n\x01s\x18\x01 \x01(\tR\x01s\x12\x16\n\x06\x65rrmsg\x18\x02 \x01(\tR\x06\x65rrmsg\x12\x35\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32!.injective_explorer_rpc.ValidatorR\x04\x64\x61ta\"5\n\x19GetValidatorUptimeRequest\x12\x18\n\x07\x61\x64\x64ress\x18\x01 \x01(\tR\x07\x61\x64\x64ress\"\x7f\n\x1aGetValidatorUptimeResponse\x12\x0c\n\x01s\x18\x01 \x01(\tR\x01s\x12\x16\n\x06\x65rrmsg\x18\x02 \x01(\tR\x06\x65rrmsg\x12;\n\x04\x64\x61ta\x18\x03 \x03(\x0b\x32\'.injective_explorer_rpc.ValidatorUptimeR\x04\x64\x61ta\"\xa3\x02\n\rGetTxsRequest\x12\x16\n\x06\x62\x65\x66ore\x18\x01 \x01(\x04R\x06\x62\x65\x66ore\x12\x14\n\x05\x61\x66ter\x18\x02 \x01(\x04R\x05\x61\x66ter\x12\x14\n\x05limit\x18\x03 \x01(\x11R\x05limit\x12\x12\n\x04skip\x18\x04 \x01(\x04R\x04skip\x12\x12\n\x04type\x18\x05 \x01(\tR\x04type\x12\x16\n\x06module\x18\x06 \x01(\tR\x06module\x12\x1f\n\x0b\x66rom_number\x18\x07 \x01(\x12R\nfromNumber\x12\x1b\n\tto_number\x18\x08 \x01(\x12R\x08toNumber\x12\x1d\n\nstart_time\x18\t \x01(\x12R\tstartTime\x12\x19\n\x08\x65nd_time\x18\n \x01(\x12R\x07\x65ndTime\x12\x16\n\x06status\x18\x0b \x01(\tR\x06status\"|\n\x0eGetTxsResponse\x12\x36\n\x06paging\x18\x01 \x01(\x0b\x32\x1e.injective_explorer_rpc.PagingR\x06paging\x12\x32\n\x04\x64\x61ta\x18\x02 \x03(\x0b\x32\x1e.injective_explorer_rpc.TxDataR\x04\x64\x61ta\"*\n\x14GetTxByTxHashRequest\x12\x12\n\x04hash\x18\x01 \x01(\tR\x04hash\"w\n\x15GetTxByTxHashResponse\x12\x0c\n\x01s\x18\x01 \x01(\tR\x01s\x12\x16\n\x06\x65rrmsg\x18\x02 \x01(\tR\x06\x65rrmsg\x12\x38\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32$.injective_explorer_rpc.TxDetailDataR\x04\x64\x61ta\"y\n\x19GetPeggyDepositTxsRequest\x12\x16\n\x06sender\x18\x01 \x01(\tR\x06sender\x12\x1a\n\x08receiver\x18\x02 \x01(\tR\x08receiver\x12\x14\n\x05limit\x18\x03 \x01(\x11R\x05limit\x12\x12\n\x04skip\x18\x04 \x01(\x04R\x04skip\"Z\n\x1aGetPeggyDepositTxsResponse\x12<\n\x05\x66ield\x18\x01 \x03(\x0b\x32&.injective_explorer_rpc.PeggyDepositTxR\x05\x66ield\"\xf9\x02\n\x0ePeggyDepositTx\x12\x16\n\x06sender\x18\x01 \x01(\tR\x06sender\x12\x1a\n\x08receiver\x18\x02 \x01(\tR\x08receiver\x12\x1f\n\x0b\x65vent_nonce\x18\x03 \x01(\x04R\neventNonce\x12!\n\x0c\x65vent_height\x18\x04 \x01(\x04R\x0b\x65ventHeight\x12\x16\n\x06\x61mount\x18\x05 \x01(\tR\x06\x61mount\x12\x14\n\x05\x64\x65nom\x18\x06 \x01(\tR\x05\x64\x65nom\x12\x31\n\x14orchestrator_address\x18\x07 \x01(\tR\x13orchestratorAddress\x12\x14\n\x05state\x18\x08 \x01(\tR\x05state\x12\x1d\n\nclaim_type\x18\t \x01(\x11R\tclaimType\x12\x1b\n\ttx_hashes\x18\n \x03(\tR\x08txHashes\x12\x1d\n\ncreated_at\x18\x0b \x01(\tR\tcreatedAt\x12\x1d\n\nupdated_at\x18\x0c \x01(\tR\tupdatedAt\"|\n\x1cGetPeggyWithdrawalTxsRequest\x12\x16\n\x06sender\x18\x01 \x01(\tR\x06sender\x12\x1a\n\x08receiver\x18\x02 \x01(\tR\x08receiver\x12\x14\n\x05limit\x18\x03 \x01(\x11R\x05limit\x12\x12\n\x04skip\x18\x04 \x01(\x04R\x04skip\"`\n\x1dGetPeggyWithdrawalTxsResponse\x12?\n\x05\x66ield\x18\x01 \x03(\x0b\x32).injective_explorer_rpc.PeggyWithdrawalTxR\x05\x66ield\"\x87\x04\n\x11PeggyWithdrawalTx\x12\x16\n\x06sender\x18\x01 \x01(\tR\x06sender\x12\x1a\n\x08receiver\x18\x02 \x01(\tR\x08receiver\x12\x16\n\x06\x61mount\x18\x03 \x01(\tR\x06\x61mount\x12\x14\n\x05\x64\x65nom\x18\x04 \x01(\tR\x05\x64\x65nom\x12\x1d\n\nbridge_fee\x18\x05 \x01(\tR\tbridgeFee\x12$\n\x0eoutgoing_tx_id\x18\x06 \x01(\x04R\x0coutgoingTxId\x12#\n\rbatch_timeout\x18\x07 \x01(\x04R\x0c\x62\x61tchTimeout\x12\x1f\n\x0b\x62\x61tch_nonce\x18\x08 \x01(\x04R\nbatchNonce\x12\x31\n\x14orchestrator_address\x18\t \x01(\tR\x13orchestratorAddress\x12\x1f\n\x0b\x65vent_nonce\x18\n \x01(\x04R\neventNonce\x12!\n\x0c\x65vent_height\x18\x0b \x01(\x04R\x0b\x65ventHeight\x12\x14\n\x05state\x18\x0c \x01(\tR\x05state\x12\x1d\n\nclaim_type\x18\r \x01(\x11R\tclaimType\x12\x1b\n\ttx_hashes\x18\x0e \x03(\tR\x08txHashes\x12\x1d\n\ncreated_at\x18\x0f \x01(\tR\tcreatedAt\x12\x1d\n\nupdated_at\x18\x10 \x01(\tR\tupdatedAt\"\xf4\x01\n\x18GetIBCTransferTxsRequest\x12\x16\n\x06sender\x18\x01 \x01(\tR\x06sender\x12\x1a\n\x08receiver\x18\x02 \x01(\tR\x08receiver\x12\x1f\n\x0bsrc_channel\x18\x03 \x01(\tR\nsrcChannel\x12\x19\n\x08src_port\x18\x04 \x01(\tR\x07srcPort\x12!\n\x0c\x64\x65st_channel\x18\x05 \x01(\tR\x0b\x64\x65stChannel\x12\x1b\n\tdest_port\x18\x06 \x01(\tR\x08\x64\x65stPort\x12\x14\n\x05limit\x18\x07 \x01(\x11R\x05limit\x12\x12\n\x04skip\x18\x08 \x01(\x04R\x04skip\"X\n\x19GetIBCTransferTxsResponse\x12;\n\x05\x66ield\x18\x01 \x03(\x0b\x32%.injective_explorer_rpc.IBCTransferTxR\x05\x66ield\"\x9e\x04\n\rIBCTransferTx\x12\x16\n\x06sender\x18\x01 \x01(\tR\x06sender\x12\x1a\n\x08receiver\x18\x02 \x01(\tR\x08receiver\x12\x1f\n\x0bsource_port\x18\x03 \x01(\tR\nsourcePort\x12%\n\x0esource_channel\x18\x04 \x01(\tR\rsourceChannel\x12)\n\x10\x64\x65stination_port\x18\x05 \x01(\tR\x0f\x64\x65stinationPort\x12/\n\x13\x64\x65stination_channel\x18\x06 \x01(\tR\x12\x64\x65stinationChannel\x12\x16\n\x06\x61mount\x18\x07 \x01(\tR\x06\x61mount\x12\x14\n\x05\x64\x65nom\x18\x08 \x01(\tR\x05\x64\x65nom\x12%\n\x0etimeout_height\x18\t \x01(\tR\rtimeoutHeight\x12+\n\x11timeout_timestamp\x18\n \x01(\x04R\x10timeoutTimestamp\x12\'\n\x0fpacket_sequence\x18\x0b \x01(\x04R\x0epacketSequence\x12\x19\n\x08\x64\x61ta_hex\x18\x0c \x01(\x0cR\x07\x64\x61taHex\x12\x14\n\x05state\x18\r \x01(\tR\x05state\x12\x1b\n\ttx_hashes\x18\x0e \x03(\tR\x08txHashes\x12\x1d\n\ncreated_at\x18\x0f \x01(\tR\tcreatedAt\x12\x1d\n\nupdated_at\x18\x10 \x01(\tR\tupdatedAt\"i\n\x13GetWasmCodesRequest\x12\x14\n\x05limit\x18\x01 \x01(\x11R\x05limit\x12\x1f\n\x0b\x66rom_number\x18\x02 \x01(\x12R\nfromNumber\x12\x1b\n\tto_number\x18\x03 \x01(\x12R\x08toNumber\"\x84\x01\n\x14GetWasmCodesResponse\x12\x36\n\x06paging\x18\x01 \x01(\x0b\x32\x1e.injective_explorer_rpc.PagingR\x06paging\x12\x34\n\x04\x64\x61ta\x18\x02 \x03(\x0b\x32 .injective_explorer_rpc.WasmCodeR\x04\x64\x61ta\"\xe2\x03\n\x08WasmCode\x12\x17\n\x07\x63ode_id\x18\x01 \x01(\x04R\x06\x63odeId\x12\x17\n\x07tx_hash\x18\x02 \x01(\tR\x06txHash\x12<\n\x08\x63hecksum\x18\x03 \x01(\x0b\x32 .injective_explorer_rpc.ChecksumR\x08\x63hecksum\x12\x1d\n\ncreated_at\x18\x04 \x01(\x04R\tcreatedAt\x12#\n\rcontract_type\x18\x05 \x01(\tR\x0c\x63ontractType\x12\x18\n\x07version\x18\x06 \x01(\tR\x07version\x12J\n\npermission\x18\x07 \x01(\x0b\x32*.injective_explorer_rpc.ContractPermissionR\npermission\x12\x1f\n\x0b\x63ode_schema\x18\x08 \x01(\tR\ncodeSchema\x12\x1b\n\tcode_view\x18\t \x01(\tR\x08\x63odeView\x12\"\n\x0cinstantiates\x18\n \x01(\x04R\x0cinstantiates\x12\x18\n\x07\x63reator\x18\x0b \x01(\tR\x07\x63reator\x12\x1f\n\x0b\x63ode_number\x18\x0c \x01(\x12R\ncodeNumber\x12\x1f\n\x0bproposal_id\x18\r \x01(\x12R\nproposalId\"<\n\x08\x43hecksum\x12\x1c\n\talgorithm\x18\x01 \x01(\tR\talgorithm\x12\x12\n\x04hash\x18\x02 \x01(\tR\x04hash\"O\n\x12\x43ontractPermission\x12\x1f\n\x0b\x61\x63\x63\x65ss_type\x18\x01 \x01(\x11R\naccessType\x12\x18\n\x07\x61\x64\x64ress\x18\x02 \x01(\tR\x07\x61\x64\x64ress\"1\n\x16GetWasmCodeByIDRequest\x12\x17\n\x07\x63ode_id\x18\x01 \x01(\x12R\x06\x63odeId\"\xf1\x03\n\x17GetWasmCodeByIDResponse\x12\x17\n\x07\x63ode_id\x18\x01 \x01(\x04R\x06\x63odeId\x12\x17\n\x07tx_hash\x18\x02 \x01(\tR\x06txHash\x12<\n\x08\x63hecksum\x18\x03 \x01(\x0b\x32 .injective_explorer_rpc.ChecksumR\x08\x63hecksum\x12\x1d\n\ncreated_at\x18\x04 \x01(\x04R\tcreatedAt\x12#\n\rcontract_type\x18\x05 \x01(\tR\x0c\x63ontractType\x12\x18\n\x07version\x18\x06 \x01(\tR\x07version\x12J\n\npermission\x18\x07 \x01(\x0b\x32*.injective_explorer_rpc.ContractPermissionR\npermission\x12\x1f\n\x0b\x63ode_schema\x18\x08 \x01(\tR\ncodeSchema\x12\x1b\n\tcode_view\x18\t \x01(\tR\x08\x63odeView\x12\"\n\x0cinstantiates\x18\n \x01(\x04R\x0cinstantiates\x12\x18\n\x07\x63reator\x18\x0b \x01(\tR\x07\x63reator\x12\x1f\n\x0b\x63ode_number\x18\x0c \x01(\x12R\ncodeNumber\x12\x1f\n\x0bproposal_id\x18\r \x01(\x12R\nproposalId\"\xd1\x01\n\x17GetWasmContractsRequest\x12\x14\n\x05limit\x18\x01 \x01(\x11R\x05limit\x12\x17\n\x07\x63ode_id\x18\x02 \x01(\x12R\x06\x63odeId\x12\x1f\n\x0b\x66rom_number\x18\x03 \x01(\x12R\nfromNumber\x12\x1b\n\tto_number\x18\x04 \x01(\x12R\x08toNumber\x12\x1f\n\x0b\x61ssets_only\x18\x05 \x01(\x08R\nassetsOnly\x12\x12\n\x04skip\x18\x06 \x01(\x12R\x04skip\x12\x14\n\x05label\x18\x07 \x01(\tR\x05label\"\x8c\x01\n\x18GetWasmContractsResponse\x12\x36\n\x06paging\x18\x01 \x01(\x0b\x32\x1e.injective_explorer_rpc.PagingR\x06paging\x12\x38\n\x04\x64\x61ta\x18\x02 \x03(\x0b\x32$.injective_explorer_rpc.WasmContractR\x04\x64\x61ta\"\xe9\x04\n\x0cWasmContract\x12\x14\n\x05label\x18\x01 \x01(\tR\x05label\x12\x18\n\x07\x61\x64\x64ress\x18\x02 \x01(\tR\x07\x61\x64\x64ress\x12\x17\n\x07tx_hash\x18\x03 \x01(\tR\x06txHash\x12\x18\n\x07\x63reator\x18\x04 \x01(\tR\x07\x63reator\x12\x1a\n\x08\x65xecutes\x18\x05 \x01(\x04R\x08\x65xecutes\x12\'\n\x0finstantiated_at\x18\x06 \x01(\x04R\x0einstantiatedAt\x12!\n\x0cinit_message\x18\x07 \x01(\tR\x0binitMessage\x12(\n\x10last_executed_at\x18\x08 \x01(\x04R\x0elastExecutedAt\x12:\n\x05\x66unds\x18\t \x03(\x0b\x32$.injective_explorer_rpc.ContractFundR\x05\x66unds\x12\x17\n\x07\x63ode_id\x18\n \x01(\x04R\x06\x63odeId\x12\x14\n\x05\x61\x64min\x18\x0b \x01(\tR\x05\x61\x64min\x12\x36\n\x17\x63urrent_migrate_message\x18\x0c \x01(\tR\x15\x63urrentMigrateMessage\x12\'\n\x0f\x63ontract_number\x18\r \x01(\x12R\x0e\x63ontractNumber\x12\x18\n\x07version\x18\x0e \x01(\tR\x07version\x12\x12\n\x04type\x18\x0f \x01(\tR\x04type\x12I\n\rcw20_metadata\x18\x10 \x01(\x0b\x32$.injective_explorer_rpc.Cw20MetadataR\x0c\x63w20Metadata\x12\x1f\n\x0bproposal_id\x18\x11 \x01(\x12R\nproposalId\"<\n\x0c\x43ontractFund\x12\x14\n\x05\x64\x65nom\x18\x01 \x01(\tR\x05\x64\x65nom\x12\x16\n\x06\x61mount\x18\x02 \x01(\tR\x06\x61mount\"\xa6\x01\n\x0c\x43w20Metadata\x12\x44\n\ntoken_info\x18\x01 \x01(\x0b\x32%.injective_explorer_rpc.Cw20TokenInfoR\ttokenInfo\x12P\n\x0emarketing_info\x18\x02 \x01(\x0b\x32).injective_explorer_rpc.Cw20MarketingInfoR\rmarketingInfo\"z\n\rCw20TokenInfo\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x16\n\x06symbol\x18\x02 \x01(\tR\x06symbol\x12\x1a\n\x08\x64\x65\x63imals\x18\x03 \x01(\x12R\x08\x64\x65\x63imals\x12!\n\x0ctotal_supply\x18\x04 \x01(\tR\x0btotalSupply\"\x81\x01\n\x11\x43w20MarketingInfo\x12\x18\n\x07project\x18\x01 \x01(\tR\x07project\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\x12\x12\n\x04logo\x18\x03 \x01(\tR\x04logo\x12\x1c\n\tmarketing\x18\x04 \x01(\x0cR\tmarketing\"L\n\x1fGetWasmContractByAddressRequest\x12)\n\x10\x63ontract_address\x18\x01 \x01(\tR\x0f\x63ontractAddress\"\xfd\x04\n GetWasmContractByAddressResponse\x12\x14\n\x05label\x18\x01 \x01(\tR\x05label\x12\x18\n\x07\x61\x64\x64ress\x18\x02 \x01(\tR\x07\x61\x64\x64ress\x12\x17\n\x07tx_hash\x18\x03 \x01(\tR\x06txHash\x12\x18\n\x07\x63reator\x18\x04 \x01(\tR\x07\x63reator\x12\x1a\n\x08\x65xecutes\x18\x05 \x01(\x04R\x08\x65xecutes\x12\'\n\x0finstantiated_at\x18\x06 \x01(\x04R\x0einstantiatedAt\x12!\n\x0cinit_message\x18\x07 \x01(\tR\x0binitMessage\x12(\n\x10last_executed_at\x18\x08 \x01(\x04R\x0elastExecutedAt\x12:\n\x05\x66unds\x18\t \x03(\x0b\x32$.injective_explorer_rpc.ContractFundR\x05\x66unds\x12\x17\n\x07\x63ode_id\x18\n \x01(\x04R\x06\x63odeId\x12\x14\n\x05\x61\x64min\x18\x0b \x01(\tR\x05\x61\x64min\x12\x36\n\x17\x63urrent_migrate_message\x18\x0c \x01(\tR\x15\x63urrentMigrateMessage\x12\'\n\x0f\x63ontract_number\x18\r \x01(\x12R\x0e\x63ontractNumber\x12\x18\n\x07version\x18\x0e \x01(\tR\x07version\x12\x12\n\x04type\x18\x0f \x01(\tR\x04type\x12I\n\rcw20_metadata\x18\x10 \x01(\x0b\x32$.injective_explorer_rpc.Cw20MetadataR\x0c\x63w20Metadata\x12\x1f\n\x0bproposal_id\x18\x11 \x01(\x12R\nproposalId\"G\n\x15GetCw20BalanceRequest\x12\x18\n\x07\x61\x64\x64ress\x18\x01 \x01(\tR\x07\x61\x64\x64ress\x12\x14\n\x05limit\x18\x02 \x01(\x11R\x05limit\"W\n\x16GetCw20BalanceResponse\x12=\n\x05\x66ield\x18\x01 \x03(\x0b\x32\'.injective_explorer_rpc.WasmCw20BalanceR\x05\x66ield\"\xda\x01\n\x0fWasmCw20Balance\x12)\n\x10\x63ontract_address\x18\x01 \x01(\tR\x0f\x63ontractAddress\x12\x18\n\x07\x61\x63\x63ount\x18\x02 \x01(\tR\x07\x61\x63\x63ount\x12\x18\n\x07\x62\x61lance\x18\x03 \x01(\tR\x07\x62\x61lance\x12\x1d\n\nupdated_at\x18\x04 \x01(\x12R\tupdatedAt\x12I\n\rcw20_metadata\x18\x05 \x01(\x0b\x32$.injective_explorer_rpc.Cw20MetadataR\x0c\x63w20Metadata\"1\n\x0fRelayersRequest\x12\x1e\n\x0bmarket_i_ds\x18\x01 \x03(\tR\tmarketIDs\"P\n\x10RelayersResponse\x12<\n\x05\x66ield\x18\x01 \x03(\x0b\x32&.injective_explorer_rpc.RelayerMarketsR\x05\x66ield\"j\n\x0eRelayerMarkets\x12\x1b\n\tmarket_id\x18\x01 \x01(\tR\x08marketId\x12;\n\x08relayers\x18\x02 \x03(\x0b\x32\x1f.injective_explorer_rpc.RelayerR\x08relayers\"/\n\x07Relayer\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x10\n\x03\x63ta\x18\x02 \x01(\tR\x03\x63ta\"\xbd\x02\n\x17GetBankTransfersRequest\x12\x18\n\x07senders\x18\x01 \x03(\tR\x07senders\x12\x1e\n\nrecipients\x18\x02 \x03(\tR\nrecipients\x12\x39\n\x19is_community_pool_related\x18\x03 \x01(\x08R\x16isCommunityPoolRelated\x12\x14\n\x05limit\x18\x04 \x01(\x11R\x05limit\x12\x12\n\x04skip\x18\x05 \x01(\x04R\x04skip\x12\x1d\n\nstart_time\x18\x06 \x01(\x12R\tstartTime\x12\x19\n\x08\x65nd_time\x18\x07 \x01(\x12R\x07\x65ndTime\x12\x18\n\x07\x61\x64\x64ress\x18\x08 \x03(\tR\x07\x61\x64\x64ress\x12\x19\n\x08per_page\x18\t \x01(\x11R\x07perPage\x12\x14\n\x05token\x18\n \x01(\tR\x05token\"\x8c\x01\n\x18GetBankTransfersResponse\x12\x36\n\x06paging\x18\x01 \x01(\x0b\x32\x1e.injective_explorer_rpc.PagingR\x06paging\x12\x38\n\x04\x64\x61ta\x18\x02 \x03(\x0b\x32$.injective_explorer_rpc.BankTransferR\x04\x64\x61ta\"\xc8\x01\n\x0c\x42\x61nkTransfer\x12\x16\n\x06sender\x18\x01 \x01(\tR\x06sender\x12\x1c\n\trecipient\x18\x02 \x01(\tR\trecipient\x12\x36\n\x07\x61mounts\x18\x03 \x03(\x0b\x32\x1c.injective_explorer_rpc.CoinR\x07\x61mounts\x12!\n\x0c\x62lock_number\x18\x04 \x01(\x04R\x0b\x62lockNumber\x12\'\n\x0f\x62lock_timestamp\x18\x05 \x01(\tR\x0e\x62lockTimestamp\"4\n\x04\x43oin\x12\x14\n\x05\x64\x65nom\x18\x01 \x01(\tR\x05\x64\x65nom\x12\x16\n\x06\x61mount\x18\x02 \x01(\tR\x06\x61mount\"\x12\n\x10StreamTxsRequest\"\xa8\x02\n\x11StreamTxsResponse\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12!\n\x0c\x62lock_number\x18\x02 \x01(\x04R\x0b\x62lockNumber\x12\'\n\x0f\x62lock_timestamp\x18\x03 \x01(\tR\x0e\x62lockTimestamp\x12\x12\n\x04hash\x18\x04 \x01(\tR\x04hash\x12\x1c\n\tcodespace\x18\x05 \x01(\tR\tcodespace\x12\x1a\n\x08messages\x18\x06 \x01(\tR\x08messages\x12\x1b\n\ttx_number\x18\x07 \x01(\x04R\x08txNumber\x12\x1b\n\terror_log\x18\x08 \x01(\tR\x08\x65rrorLog\x12\x12\n\x04\x63ode\x18\t \x01(\rR\x04\x63ode\x12\x1b\n\tclaim_ids\x18\n \x03(\x12R\x08\x63laimIds\"\x15\n\x13StreamBlocksRequest\"\xb8\x02\n\x14StreamBlocksResponse\x12\x16\n\x06height\x18\x01 \x01(\x04R\x06height\x12\x1a\n\x08proposer\x18\x02 \x01(\tR\x08proposer\x12\x18\n\x07moniker\x18\x03 \x01(\tR\x07moniker\x12\x1d\n\nblock_hash\x18\x04 \x01(\tR\tblockHash\x12\x1f\n\x0bparent_hash\x18\x05 \x01(\tR\nparentHash\x12&\n\x0fnum_pre_commits\x18\x06 \x01(\x12R\rnumPreCommits\x12\x17\n\x07num_txs\x18\x07 \x01(\x12R\x06numTxs\x12\x33\n\x03txs\x18\x08 \x03(\x0b\x32!.injective_explorer_rpc.TxDataRPCR\x03txs\x12\x1c\n\ttimestamp\x18\t \x01(\tR\ttimestamp2\xc6\x13\n\x14InjectiveExplorerRPC\x12l\n\rGetAccountTxs\x12,.injective_explorer_rpc.GetAccountTxsRequest\x1a-.injective_explorer_rpc.GetAccountTxsResponse\x12o\n\x0eGetContractTxs\x12-.injective_explorer_rpc.GetContractTxsRequest\x1a..injective_explorer_rpc.GetContractTxsResponse\x12u\n\x10GetContractTxsV2\x12/.injective_explorer_rpc.GetContractTxsV2Request\x1a\x30.injective_explorer_rpc.GetContractTxsV2Response\x12`\n\tGetBlocks\x12(.injective_explorer_rpc.GetBlocksRequest\x1a).injective_explorer_rpc.GetBlocksResponse\x12]\n\x08GetBlock\x12\'.injective_explorer_rpc.GetBlockRequest\x1a(.injective_explorer_rpc.GetBlockResponse\x12l\n\rGetValidators\x12,.injective_explorer_rpc.GetValidatorsRequest\x1a-.injective_explorer_rpc.GetValidatorsResponse\x12i\n\x0cGetValidator\x12+.injective_explorer_rpc.GetValidatorRequest\x1a,.injective_explorer_rpc.GetValidatorResponse\x12{\n\x12GetValidatorUptime\x12\x31.injective_explorer_rpc.GetValidatorUptimeRequest\x1a\x32.injective_explorer_rpc.GetValidatorUptimeResponse\x12W\n\x06GetTxs\x12%.injective_explorer_rpc.GetTxsRequest\x1a&.injective_explorer_rpc.GetTxsResponse\x12l\n\rGetTxByTxHash\x12,.injective_explorer_rpc.GetTxByTxHashRequest\x1a-.injective_explorer_rpc.GetTxByTxHashResponse\x12{\n\x12GetPeggyDepositTxs\x12\x31.injective_explorer_rpc.GetPeggyDepositTxsRequest\x1a\x32.injective_explorer_rpc.GetPeggyDepositTxsResponse\x12\x84\x01\n\x15GetPeggyWithdrawalTxs\x12\x34.injective_explorer_rpc.GetPeggyWithdrawalTxsRequest\x1a\x35.injective_explorer_rpc.GetPeggyWithdrawalTxsResponse\x12x\n\x11GetIBCTransferTxs\x12\x30.injective_explorer_rpc.GetIBCTransferTxsRequest\x1a\x31.injective_explorer_rpc.GetIBCTransferTxsResponse\x12i\n\x0cGetWasmCodes\x12+.injective_explorer_rpc.GetWasmCodesRequest\x1a,.injective_explorer_rpc.GetWasmCodesResponse\x12r\n\x0fGetWasmCodeByID\x12..injective_explorer_rpc.GetWasmCodeByIDRequest\x1a/.injective_explorer_rpc.GetWasmCodeByIDResponse\x12u\n\x10GetWasmContracts\x12/.injective_explorer_rpc.GetWasmContractsRequest\x1a\x30.injective_explorer_rpc.GetWasmContractsResponse\x12\x8d\x01\n\x18GetWasmContractByAddress\x12\x37.injective_explorer_rpc.GetWasmContractByAddressRequest\x1a\x38.injective_explorer_rpc.GetWasmContractByAddressResponse\x12o\n\x0eGetCw20Balance\x12-.injective_explorer_rpc.GetCw20BalanceRequest\x1a..injective_explorer_rpc.GetCw20BalanceResponse\x12]\n\x08Relayers\x12\'.injective_explorer_rpc.RelayersRequest\x1a(.injective_explorer_rpc.RelayersResponse\x12u\n\x10GetBankTransfers\x12/.injective_explorer_rpc.GetBankTransfersRequest\x1a\x30.injective_explorer_rpc.GetBankTransfersResponse\x12\x62\n\tStreamTxs\x12(.injective_explorer_rpc.StreamTxsRequest\x1a).injective_explorer_rpc.StreamTxsResponse0\x01\x12k\n\x0cStreamBlocks\x12+.injective_explorer_rpc.StreamBlocksRequest\x1a,.injective_explorer_rpc.StreamBlocksResponse0\x01\x42\xc2\x01\n\x1a\x63om.injective_explorer_rpcB\x19InjectiveExplorerRpcProtoP\x01Z\x19/injective_explorer_rpcpb\xa2\x02\x03IXX\xaa\x02\x14InjectiveExplorerRpc\xca\x02\x14InjectiveExplorerRpc\xe2\x02 InjectiveExplorerRpc\\GPBMetadata\xea\x02\x14InjectiveExplorerRpcb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'exchange.injective_explorer_rpc_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\032com.injective_explorer_rpcB\031InjectiveExplorerRpcProtoP\001Z\031/injective_explorer_rpcpb\242\002\003IXX\252\002\024InjectiveExplorerRpc\312\002\024InjectiveExplorerRpc\342\002 InjectiveExplorerRpc\\GPBMetadata\352\002\024InjectiveExplorerRpc'
  _globals['_EVENT_ATTRIBUTESENTRY']._loaded_options = None
  _globals['_EVENT_ATTRIBUTESENTRY']._serialized_options = b'8\001'
  _globals['_GETACCOUNTTXSREQUEST']._serialized_start=66
  _globals['_GETACCOUNTTXSREQUEST']._serialized_end=390
  _globals['_GETACCOUNTTXSRESPONSE']._serialized_start=393
  _globals['_GETACCOUNTTXSRESPONSE']._serialized_end=530
  _globals['_PAGING']._serialized_start=533
  _globals['_PAGING']._serialized_end=667
  _globals['_TXDETAILDATA']._serialized_start=670
  _globals['_TXDETAILDATA']._serialized_end=1353
  _globals['_GASFEE']._serialized_start=1356
  _globals['_GASFEE']._serialized_end=1501
  _globals['_COSMOSCOIN']._serialized_start=1503
  _globals['_COSMOSCOIN']._serialized_end=1561
  _globals['_EVENT']._serialized_start=1564
  _globals['_EVENT']._serialized_end=1733
  _globals['_EVENT_ATTRIBUTESENTRY']._serialized_start=1672
  _globals['_EVENT_ATTRIBUTESENTRY']._serialized_end=1733
  _globals['_SIGNATURE']._serialized_start=1735
  _globals['_SIGNATURE']._serialized_end=1854
  _globals['_GETCONTRACTTXSREQUEST']._serialized_start=1857
  _globals['_GETCONTRACTTXSREQUEST']._serialized_end=2010
  _globals['_GETCONTRACTTXSRESPONSE']._serialized_start=2013
  _globals['_GETCONTRACTTXSRESPONSE']._serialized_end=2151
  _globals['_GETCONTRACTTXSV2REQUEST']._serialized_start=2154
  _globals['_GETCONTRACTTXSV2REQUEST']._serialized_end=2309
  _globals['_GETCONTRACTTXSV2RESPONSE']._serialized_start=2311
  _globals['_GETCONTRACTTXSV2RESPONSE']._serialized_end=2415
  _globals['_GETBLOCKSREQUEST']._serialized_start=2417
  _globals['_GETBLOCKSREQUEST']._serialized_end=2539
  _globals['_GETBLOCKSRESPONSE']._serialized_start=2542
  _globals['_GETBLOCKSRESPONSE']._serialized_end=2672
  _globals['_BLOCKINFO']._serialized_start=2675
  _globals['_BLOCKINFO']._serialized_end=2976
  _globals['_TXDATARPC']._serialized_start=2979
  _globals['_TXDATARPC']._serialized_end=3267
  _globals['_GETBLOCKREQUEST']._serialized_start=3269
  _globals['_GETBLOCKREQUEST']._serialized_end=3302
  _globals['_GETBLOCKRESPONSE']._serialized_start=3304
  _globals['_GETBLOCKRESPONSE']._serialized_end=3421
  _globals['_BLOCKDETAILINFO']._serialized_start=3424
  _globals['_BLOCKDETAILINFO']._serialized_end=3757
  _globals['_TXDATA']._serialized_start=3760
  _globals['_TXDATA']._serialized_end=4099
  _globals['_GETVALIDATORSREQUEST']._serialized_start=4101
  _globals['_GETVALIDATORSREQUEST']._serialized_end=4123
  _globals['_GETVALIDATORSRESPONSE']._serialized_start=4125
  _globals['_GETVALIDATORSRESPONSE']._serialized_end=4241
  _globals['_VALIDATOR']._serialized_start=4244
  _globals['_VALIDATOR']._serialized_end=5193
  _globals['_VALIDATORDESCRIPTION']._serialized_start=5196
  _globals['_VALIDATORDESCRIPTION']._serialized_end=5396
  _globals['_VALIDATORUPTIME']._serialized_start=5398
  _globals['_VALIDATORUPTIME']._serialized_end=5474
  _globals['_SLASHINGEVENT']._serialized_start=5477
  _globals['_SLASHINGEVENT']._serialized_end=5701
  _globals['_GETVALIDATORREQUEST']._serialized_start=5703
  _globals['_GETVALIDATORREQUEST']._serialized_end=5750
  _globals['_GETVALIDATORRESPONSE']._serialized_start=5752
  _globals['_GETVALIDATORRESPONSE']._serialized_end=5867
  _globals['_GETVALIDATORUPTIMEREQUEST']._serialized_start=5869
  _globals['_GETVALIDATORUPTIMEREQUEST']._serialized_end=5922
  _globals['_GETVALIDATORUPTIMERESPONSE']._serialized_start=5924
  _globals['_GETVALIDATORUPTIMERESPONSE']._serialized_end=6051
  _globals['_GETTXSREQUEST']._serialized_start=6054
  _globals['_GETTXSREQUEST']._serialized_end=6345
  _globals['_GETTXSRESPONSE']._serialized_start=6347
  _globals['_GETTXSRESPONSE']._serialized_end=6471
  _globals['_GETTXBYTXHASHREQUEST']._serialized_start=6473
  _globals['_GETTXBYTXHASHREQUEST']._serialized_end=6515
  _globals['_GETTXBYTXHASHRESPONSE']._serialized_start=6517
  _globals['_GETTXBYTXHASHRESPONSE']._serialized_end=6636
  _globals['_GETPEGGYDEPOSITTXSREQUEST']._serialized_start=6638
  _globals['_GETPEGGYDEPOSITTXSREQUEST']._serialized_end=6759
  _globals['_GETPEGGYDEPOSITTXSRESPONSE']._serialized_start=6761
  _globals['_GETPEGGYDEPOSITTXSRESPONSE']._serialized_end=6851
  _globals['_PEGGYDEPOSITTX']._serialized_start=6854
  _globals['_PEGGYDEPOSITTX']._serialized_end=7231
  _globals['_GETPEGGYWITHDRAWALTXSREQUEST']._serialized_start=7233
  _globals['_GETPEGGYWITHDRAWALTXSREQUEST']._serialized_end=7357
  _globals['_GETPEGGYWITHDRAWALTXSRESPONSE']._serialized_start=7359
  _globals['_GETPEGGYWITHDRAWALTXSRESPONSE']._serialized_end=7455
  _globals['_PEGGYWITHDRAWALTX']._serialized_start=7458
  _globals['_PEGGYWITHDRAWALTX']._serialized_end=7977
  _globals['_GETIBCTRANSFERTXSREQUEST']._serialized_start=7980
  _globals['_GETIBCTRANSFERTXSREQUEST']._serialized_end=8224
  _globals['_GETIBCTRANSFERTXSRESPONSE']._serialized_start=8226
  _globals['_GETIBCTRANSFERTXSRESPONSE']._serialized_end=8314
  _globals['_IBCTRANSFERTX']._serialized_start=8317
  _globals['_IBCTRANSFERTX']._serialized_end=8859
  _globals['_GETWASMCODESREQUEST']._serialized_start=8861
  _globals['_GETWASMCODESREQUEST']._serialized_end=8966
  _globals['_GETWASMCODESRESPONSE']._serialized_start=8969
  _globals['_GETWASMCODESRESPONSE']._serialized_end=9101
  _globals['_WASMCODE']._serialized_start=9104
  _globals['_WASMCODE']._serialized_end=9586
  _globals['_CHECKSUM']._serialized_start=9588
  _globals['_CHECKSUM']._serialized_end=9648
  _globals['_CONTRACTPERMISSION']._serialized_start=9650
  _globals['_CONTRACTPERMISSION']._serialized_end=9729
  _globals['_GETWASMCODEBYIDREQUEST']._serialized_start=9731
  _globals['_GETWASMCODEBYIDREQUEST']._serialized_end=9780
  _globals['_GETWASMCODEBYIDRESPONSE']._serialized_start=9783
  _globals['_GETWASMCODEBYIDRESPONSE']._serialized_end=10280
  _globals['_GETWASMCONTRACTSREQUEST']._serialized_start=10283
  _globals['_GETWASMCONTRACTSREQUEST']._serialized_end=10492
  _globals['_GETWASMCONTRACTSRESPONSE']._serialized_start=10495
  _globals['_GETWASMCONTRACTSRESPONSE']._serialized_end=10635
  _globals['_WASMCONTRACT']._serialized_start=10638
  _globals['_WASMCONTRACT']._serialized_end=11255
  _globals['_CONTRACTFUND']._serialized_start=11257
  _globals['_CONTRACTFUND']._serialized_end=11317
  _globals['_CW20METADATA']._serialized_start=11320
  _globals['_CW20METADATA']._serialized_end=11486
  _globals['_CW20TOKENINFO']._serialized_start=11488
  _globals['_CW20TOKENINFO']._serialized_end=11610
  _globals['_CW20MARKETINGINFO']._serialized_start=11613
  _globals['_CW20MARKETINGINFO']._serialized_end=11742
  _globals['_GETWASMCONTRACTBYADDRESSREQUEST']._serialized_start=11744
  _globals['_GETWASMCONTRACTBYADDRESSREQUEST']._serialized_end=11820
  _globals['_GETWASMCONTRACTBYADDRESSRESPONSE']._serialized_start=11823
  _globals['_GETWASMCONTRACTBYADDRESSRESPONSE']._serialized_end=12460
  _globals['_GETCW20BALANCEREQUEST']._serialized_start=12462
  _globals['_GETCW20BALANCEREQUEST']._serialized_end=12533
  _globals['_GETCW20BALANCERESPONSE']._serialized_start=12535
  _globals['_GETCW20BALANCERESPONSE']._serialized_end=12622
  _globals['_WASMCW20BALANCE']._serialized_start=12625
  _globals['_WASMCW20BALANCE']._serialized_end=12843
  _globals['_RELAYERSREQUEST']._serialized_start=12845
  _globals['_RELAYERSREQUEST']._serialized_end=12894
  _globals['_RELAYERSRESPONSE']._serialized_start=12896
  _globals['_RELAYERSRESPONSE']._serialized_end=12976
  _globals['_RELAYERMARKETS']._serialized_start=12978
  _globals['_RELAYERMARKETS']._serialized_end=13084
  _globals['_RELAYER']._serialized_start=13086
  _globals['_RELAYER']._serialized_end=13133
  _globals['_GETBANKTRANSFERSREQUEST']._serialized_start=13136
  _globals['_GETBANKTRANSFERSREQUEST']._serialized_end=13453
  _globals['_GETBANKTRANSFERSRESPONSE']._serialized_start=13456
  _globals['_GETBANKTRANSFERSRESPONSE']._serialized_end=13596
  _globals['_BANKTRANSFER']._serialized_start=13599
  _globals['_BANKTRANSFER']._serialized_end=13799
  _globals['_COIN']._serialized_start=13801
  _globals['_COIN']._serialized_end=13853
  _globals['_STREAMTXSREQUEST']._serialized_start=13855
  _globals['_STREAMTXSREQUEST']._serialized_end=13873
  _globals['_STREAMTXSRESPONSE']._serialized_start=13876
  _globals['_STREAMTXSRESPONSE']._serialized_end=14172
  _globals['_STREAMBLOCKSREQUEST']._serialized_start=14174
  _globals['_STREAMBLOCKSREQUEST']._serialized_end=14195
  _globals['_STREAMBLOCKSRESPONSE']._serialized_start=14198
  _globals['_STREAMBLOCKSRESPONSE']._serialized_end=14510
  _globals['_INJECTIVEEXPLORERRPC']._serialized_start=14513
  _globals['_INJECTIVEEXPLORERRPC']._serialized_end=17015
# @@protoc_insertion_point(module_scope)
