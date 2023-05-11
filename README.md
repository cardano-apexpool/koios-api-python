# koios-api-python
A python package for the Cardano Blockchain Koios API (https://api.koios.rest/)

## Install
To install the module, type the following command:
```bash
pip3 install koios_api
```
## Environment
By default, koios_api works with mainnet, but it can also work with the preview and preprod testnets, and even with custom Api URLs (because anyone can install an own Koios Api).
To use a testnet you can set the environment variable:

```bash
#preprod
export CARDANO_NET=preprod
```

```bash
#preview
export CARDANO_NET=preview
```

To work with a custom Api URL, set the environment variable:

```bash
export API_BASE_URL=https://custom.url/api/v0
```

## Using the module
Importing the complete module:
```python
import koios_api
koios_api.get_tip()
```
The result will be like this:
```json
[
  {
    "hash": "442765ab5660346a6af3ba7667bbd35934e6219a52f0f53a80f28d27a70309c1",
    "epoch_no": 381,
    "abs_slot": 79265882,
    "epoch_slot": 37082,
    "block_no": 8129347,
    "block_time": 1670832173
  }
]
```
Import only specific functions:
```python
from koios_api.network import get_tip
get_tip()
```
The result will be identical.

## Modules

[Network](#Network)<br>
[get_tip](#get_tip) Get the tip info about the latest block seen by chain<br>
[get_genesis](#get_genesis) Get the Genesis parameters used to start specific era on chain<br>
[get_totals](#get_totals) Get the circulating utxo, treasury, rewards, supply and reserves in lovelace for specified epoch, all epochs if empty<br>
[get_param_updates](#get_param_updates) Get all parameter update proposals submitted to the chain starting Shelley era<br>

[Epoch](#Epoch)<br>
[get_epoch_info](#get_epoch_info) Get the epoch information, all epochs if no epoch specified<br>
[get_epoch_params](#get_epoch_params) Get the protocol parameters for specific epoch, returns information about all epochs if no epoch specified<br>
[get_epoch_block_protocols](#get_epoch_block_protocols) Get the information about block protocol distribution in epoch<br>

[Block](#Block)<br>
[get_blocks](#get_blocks) Get summarised details about all blocks (paginated, the latest first)<br>
[get_block_info](#get_block_info) Get detailed information about a specific block<br>
[get_block_txs](#get_block_txs) Get a list of all transactions included in provided blocks<br>

[Transactions](#Transactions)<br>
[get_tx_info](#get_tx_info) Get detailed information about transaction(s)<br>
[get_tx_utxos](#get_tx_utxos) Get UTxO set (inputs/outputs) of transactions<br>
[get_tx_metadata](#get_tx_metadata) Get metadata information (if any) for given transaction(s)<br>
[get_tx_metalabels](#get_tx_metalabels) Get a list of all transaction metadata labels<br>
[submit_tx](#submit_tx) Submit an already serialized transaction to the network<br>
[get_tx_status](#get_tx_status) Get the number of block confirmations for a given transaction hash list<br>

[Address](#Address)<br>
[get_address_info](#get_address_info) Get the transaction hash list of input address array, optionally filtering after specified block height (inclusive)<br>
[get_address_txs](#get_address_txs) Get the transaction hash list of input address array, optionally filtering after specified block height (inclusive)<br>
[get_credential_utxos](#get_credential_utxos) Get a list of UTxO against input payment credential array including their balances<br>
[get_address_assets](#get_address_assets) Get the list of all the assets (policy, name and quantity) for given addresses<br>
[get_credential_txs](#get_credential_txs) Get the transaction hash list of input payment credential array, optionally filtering after specified block height (inclusive)<br>

[Asset](#Asset)<br>
[get_asset_list](#get_asset_list) Get the list of all native assets (paginated)<br>
[get_asset_token_registry](#get_asset_token_registry) Get a list of assets registered via token registry on github<br>
[get_asset_addresses](#get_asset_addresses) Get the list of all addresses holding a given asset<br>
[get_asset_nft_address](#get_asset_nft_address) Get the address where specified NFT currently reside on.<br>
[get_asset_info](#get_asset_info) Get the information of an asset including first minting & token registry metadata<br>
[get_asset_info_bulk](#get_asset_info_bulk) Get the information of a list of assets including first minting & token registry metadata<br>
[get_asset_history](#get_asset_history) Get the mint/burn history of an asset<br>
[get_policy_asset_addresses](#get_policy_asset_addresses) Get the list of addresses with quantity for each asset on the given policy<br>
[get_policy_asset_info](#get_policy_asset_info) Get the information for all assets under the same policy<br>
[get_policy_asset_list](#get_policy_asset_list) Get the list of asset under the given policy (including balances)<br>
[get_asset_summary](#get_asset_summary) Get the summary of an asset (total transactions exclude minting/total wallets include only wallets with asset balance)<br>
[get_asset_txs](#get_asset_txs) Get the list of all asset transaction hashes (the newest first)<br>

[Pool](#Pool)<br>
[get_pools_list](#get_pools_list) A list of all currently registered/retiring (not retired) pools<br>
[get_pool_info](#get_pool_info) Current pool statuses and details for a specified list of pool ids<br>
[get_pool_stake_snapshot](#get_pool_stake_snapshot) Returns Mark, Set and Go stake snapshots for the selected pool, useful for leaderlog calculation<br>
[get_pool_delegators](#get_pool_delegators) Returns information about live delegators for a given pool<br>
[get_pool_delegators_history](#get_pool_delegators_history) Returns information about active delegators (incl. history) for a given pool and epoch number (all epochs if not specified)<br>
[get_pool_blocks](#get_pool_blocks) Returns information about blocks minted by a given pool for all epochs (or _epoch_no if provided)<br>
[get_pool_history](#get_pool_history) Returns information about pool stake, block and reward history in a given epoch (or all epochs that pool existed for, in descending order if no epoch number was provided)<br>
[get_pool_updates](#get_pool_updates) Returns all pool updates for all pools or only updates for specific pool if specified<br>
[get_pool_relays](#get_pool_relays) A list of registered relays for all currently registered/retiring (not retired) pools<br>
[get_pool_metadata](#get_pool_metadata) A list of registered relays for all currently registered/retiring (not retired) pools<br>
[get_retiring_pools](#get_retiring_pools) Get the retiring stake pools list<br>

[Script](#Script)<br>
[get_native_script_list](#get_native_script_list) The list of all existing native script hashes along with their creation transaction hashes<br>
[get_plutus_script_list](#get_plutus_script_list) The list of all existing native script hashes along with their creation transaction hashes<br>
[get_script_redeemers](#get_script_redeemers) The list of all redeemers for a given script hash<br>
[get_datum_info](#get_datum_info) The list of datum information for given datum hashes<br>

[Stake Account](#Stake Account)<br>
[get_account_list](#get_account_list) Get a list of all accounts<br>
[get_account_info](#get_account_info) Get the account information for given stake addresses (accounts)<br>
[get_account_utxos](#get_account_utxos) Get a list of all UTxOs for a given stake address (account)<br>
[get_account_info_cached](#get_account_info_cached) Get the cached account information for given stake addresses (accounts)<br>
[get_account_rewards](#get_account_rewards) Get the full rewards history (including MIR) for given stake addresses (accounts)<br>
[get_account_updates](#get_account_updates) Get the account updates (registration, deregistration, delegation and withdrawals) for given stake addresses (accounts)<br>
[get_account_addresses](#get_account_addresses) Get all addresses associated with given staking accounts<br>
[get_account_assets](#get_account_assets) Get the native asset balance of given accounts<br>
[get_account_history](#get_account_history) Get the staking history of given stake addresses (accounts)<br>

### Network

#### get_tip
Get the tip info about the latest block seen by chain<br>
Parameters: none<br>
Returns: The tip information as a list of one dictionary<br>
Example:<br>
`tip = get_tip()`<br>
Example response:
```json
[
  {
    "hash": "442765ab5660346a6af3ba7667bbd35934e6219a52f0f53a80f28d27a70309c1",
    "epoch_no": 381,
    "abs_slot": 79265882,
    "epoch_slot": 37082,
    "block_no": 8129347,
    "block_time": 1670832173
  }
]
```

#### get_genesis
Get the Genesis parameters used to start specific era on chain<br>
Parameters: none<br>
Returns: Genesis parameters used to start each era on chain as a list of one dictionary<br>
Example:<br>
`genesis = get_genesis()`<br>
Example response:
```json
[
  {
    "networkmagic": "764824073",
    "networkid": "Mainnet",
    "activeslotcoeff": "0.05",
    "updatequorum": "5",
    "maxlovelacesupply": "45000000000000000",
    "epochlength": "432000",
    "systemstart": 1506203091,
    "slotsperkesperiod": "129600",
    "slotlength": "1",
    "maxkesrevolutions": "62",
    "securityparam": "2160",
    "alonzogenesis": "{\"lovelacePerUTxOWord\":34482,\"executionPrices\":{\"prSteps\":{\"numerator\":721,\"denominator\":10000000},\"prMem\":{\"numerator\":577,\"denominator\":10000}},\"maxTxExUnits\":{\"exUnitsMem\":10000000,\"exUnitsSteps\":10000000000},\"maxBlockExUnits\":{\"exUnitsMem\":50000000,\"exUnitsSteps\":40000000000},\"maxValueSize\":5000,\"collateralPercentage\":150,\"maxCollateralInputs\":3,\"costModels\":{\"PlutusV1\":{\"sha2_256-memory-arguments\":4,\"equalsString-cpu-arguments-constant\":1000,\"cekDelayCost-exBudgetMemory\":100,\"lessThanEqualsByteString-cpu-arguments-intercept\":103599,\"divideInteger-memory-arguments-minimum\":1,\"appendByteString-cpu-arguments-slope\":621,\"blake2b-cpu-arguments-slope\":29175,\"iData-cpu-arguments\":150000,\"encodeUtf8-cpu-arguments-slope\":1000,\"unBData-cpu-arguments\":150000,\"multiplyInteger-cpu-arguments-intercept\":61516,\"cekConstCost-exBudgetMemory\":100,\"nullList-cpu-arguments\":150000,\"equalsString-cpu-arguments-intercept\":150000,\"trace-cpu-arguments\":150000,\"mkNilData-memory-arguments\":32,\"lengthOfByteString-cpu-arguments\":150000,\"cekBuiltinCost-exBudgetCPU\":29773,\"bData-cpu-arguments\":150000,\"subtractInteger-cpu-arguments-slope\":0,\"unIData-cpu-arguments\":150000,\"consByteString-memory-arguments-intercept\":0,\"divideInteger-memory-arguments-slope\":1,\"divideInteger-cpu-arguments-model-arguments-slope\":118,\"listData-cpu-arguments\":150000,\"headList-cpu-arguments\":150000,\"chooseData-memory-arguments\":32,\"equalsInteger-cpu-arguments-intercept\":136542,\"sha3_256-cpu-arguments-slope\":82363,\"sliceByteString-cpu-arguments-slope\":5000,\"unMapData-cpu-arguments\":150000,\"lessThanInteger-cpu-arguments-intercept\":179690,\"mkCons-cpu-arguments\":150000,\"appendString-memory-arguments-intercept\":0,\"modInteger-cpu-arguments-model-arguments-slope\":118,\"ifThenElse-cpu-arguments\":1,\"mkNilPairData-cpu-arguments\":150000,\"lessThanEqualsInteger-cpu-arguments-intercept\":145276,\"addInteger-memory-arguments-slope\":1,\"chooseList-memory-arguments\":32,\"constrData-memory-arguments\":32,\"decodeUtf8-cpu-arguments-intercept\":150000,\"equalsData-memory-arguments\":1,\"subtractInteger-memory-arguments-slope\":1,\"appendByteString-memory-arguments-intercept\":0,\"lengthOfByteString-memory-arguments\":4,\"headList-memory-arguments\":32,\"listData-memory-arguments\":32,\"consByteString-cpu-arguments-intercept\":150000,\"unIData-memory-arguments\":32,\"remainderInteger-memory-arguments-minimum\":1,\"bData-memory-arguments\":32,\"lessThanByteString-cpu-arguments-slope\":248,\"encodeUtf8-memory-arguments-intercept\":0,\"cekStartupCost-exBudgetCPU\":100,\"multiplyInteger-memory-arguments-intercept\":0,\"unListData-memory-arguments\":32,\"remainderInteger-cpu-arguments-model-arguments-slope\":118,\"cekVarCost-exBudgetCPU\":29773,\"remainderInteger-memory-arguments-slope\":1,\"cekForceCost-exBudgetCPU\":29773,\"sha2_256-cpu-arguments-slope\":29175,\"equalsInteger-memory-arguments\":1,\"indexByteString-memory-arguments\":1,\"addInteger-memory-arguments-intercept\":1,\"chooseUnit-cpu-arguments\":150000,\"sndPair-cpu-arguments\":150000,\"cekLamCost-exBudgetCPU\":29773,\"fstPair-cpu-arguments\":150000,\"quotientInteger-memory-arguments-minimum\":1,\"decodeUtf8-cpu-arguments-slope\":1000,\"lessThanInteger-memory-arguments\":1,\"lessThanEqualsInteger-cpu-arguments-slope\":1366,\"fstPair-memory-arguments\":32,\"modInteger-memory-arguments-intercept\":0,\"unConstrData-cpu-arguments\":150000,\"lessThanEqualsInteger-memory-arguments\":1,\"chooseUnit-memory-arguments\":32,\"sndPair-memory-arguments\":32,\"addInteger-cpu-arguments-intercept\":197209,\"decodeUtf8-memory-arguments-slope\":8,\"equalsData-cpu-arguments-intercept\":150000,\"mapData-cpu-arguments\":150000,\"mkPairData-cpu-arguments\":150000,\"quotientInteger-cpu-arguments-constant\":148000,\"consByteString-memory-arguments-slope\":1,\"cekVarCost-exBudgetMemory\":100,\"indexByteString-cpu-arguments\":150000,\"unListData-cpu-arguments\":150000,\"equalsInteger-cpu-arguments-slope\":1326,\"cekStartupCost-exBudgetMemory\":100,\"subtractInteger-cpu-arguments-intercept\":197209,\"divideInteger-cpu-arguments-model-arguments-intercept\":425507,\"divideInteger-memory-arguments-intercept\":0,\"cekForceCost-exBudgetMemory\":100,\"blake2b-cpu-arguments-intercept\":2477736,\"remainderInteger-cpu-arguments-constant\":148000,\"tailList-cpu-arguments\":150000,\"encodeUtf8-cpu-arguments-intercept\":150000,\"equalsString-cpu-arguments-slope\":1000,\"lessThanByteString-memory-arguments\":1,\"multiplyInteger-cpu-arguments-slope\":11218,\"appendByteString-cpu-arguments-intercept\":396231,\"lessThanEqualsByteString-cpu-arguments-slope\":248,\"modInteger-memory-arguments-slope\":1,\"addInteger-cpu-arguments-slope\":0,\"equalsData-cpu-arguments-slope\":10000,\"decodeUtf8-memory-arguments-intercept\":0,\"chooseList-cpu-arguments\":150000,\"constrData-cpu-arguments\":150000,\"equalsByteString-memory-arguments\":1,\"cekApplyCost-exBudgetCPU\":29773,\"quotientInteger-memory-arguments-slope\":1,\"verifySignature-cpu-arguments-intercept\":3345831,\"unMapData-memory-arguments\":32,\"mkCons-memory-arguments\":32,\"sliceByteString-memory-arguments-slope\":1,\"sha3_256-memory-arguments\":4,\"ifThenElse-memory-arguments\":1,\"mkNilPairData-memory-arguments\":32,\"equalsByteString-cpu-arguments-slope\":247,\"appendString-cpu-arguments-intercept\":150000,\"quotientInteger-cpu-arguments-model-arguments-slope\":118,\"cekApplyCost-exBudgetMemory\":100,\"equalsString-memory-arguments\":1,\"multiplyInteger-memory-arguments-slope\":1,\"cekBuiltinCost-exBudgetMemory\":100,\"remainderInteger-memory-arguments-intercept\":0,\"sha2_256-cpu-arguments-intercept\":2477736,\"remainderInteger-cpu-arguments-model-arguments-intercept\":425507,\"lessThanEqualsByteString-memory-arguments\":1,\"tailList-memory-arguments\":32,\"mkNilData-cpu-arguments\":150000,\"chooseData-cpu-arguments\":150000,\"unBData-memory-arguments\":32,\"blake2b-memory-arguments\":4,\"iData-memory-arguments\":32,\"nullList-memory-arguments\":32,\"cekDelayCost-exBudgetCPU\":29773,\"subtractInteger-memory-arguments-intercept\":1,\"lessThanByteString-cpu-arguments-intercept\":103599,\"consByteString-cpu-arguments-slope\":1000,\"appendByteString-memory-arguments-slope\":1,\"trace-memory-arguments\":32,\"divideInteger-cpu-arguments-constant\":148000,\"cekConstCost-exBudgetCPU\":29773,\"encodeUtf8-memory-arguments-slope\":8,\"quotientInteger-cpu-arguments-model-arguments-intercept\":425507,\"mapData-memory-arguments\":32,\"appendString-cpu-arguments-slope\":1000,\"modInteger-cpu-arguments-constant\":148000,\"verifySignature-cpu-arguments-slope\":1,\"unConstrData-memory-arguments\":32,\"quotientInteger-memory-arguments-intercept\":0,\"equalsByteString-cpu-arguments-constant\":150000,\"sliceByteString-memory-arguments-intercept\":0,\"mkPairData-memory-arguments\":32,\"equalsByteString-cpu-arguments-intercept\":112536,\"appendString-memory-arguments-slope\":1,\"lessThanInteger-cpu-arguments-slope\":497,\"modInteger-cpu-arguments-model-arguments-intercept\":425507,\"modInteger-memory-arguments-minimum\":1,\"sha3_256-cpu-arguments-intercept\":0,\"verifySignature-memory-arguments\":1,\"cekLamCost-exBudgetMemory\":100,\"sliceByteString-cpu-arguments-intercept\":150000}}}"
  }
]
```

#### get_totals
Get the circulating utxo, treasury, rewards, supply and reserves in lovelace for specified epoch, all epochs if empty<br>
Parameters: Epoch (optional)<br>
Returns: Supply/reserves/utxo/fees/treasury stats as a list of one dictionary (if the epoch is specified) or a list of all available epochs (if the epoch parameter is not specified)<br>
Example:<br>
`totals = get_totals(380)`<br>
Example response:
```json
[
  {
    "epoch_no": 380,
    "circulation": "33505907705011256",
    "treasury": "1085266054287657",
    "reward": "635180192555825",
    "supply": "35230640457275590",
    "reserves": "9769359542724410"
  }
]
```

#### get_param_updates
Get all parameter update proposals submitted to the chain starting Shelley era<br>
Parameters: none<br>
Returns: All parameter update proposals<br>
Example:<br>
`param_updates = get_param_updates()`<br>
```json
[
  {
    "tx_hash": "b516588da34b58b7d32b6a057f513e16ea8c87de46615631be3316d8a8847d46",
    "block_height": 4533644,
    "block_time": 1596923351,
    "epoch_no": 210,
    "data": {
      "decentralisation": 0.9
    }
  },
  {
    "tx_hash": "784902982af484f78d10f1587072f5a6b888ed0c1296d4ecf1e21c0251696ca1",
    "block_height": 4558648,
    "block_time": 1597425824,
    "epoch_no": 211,
    "data": {
      "decentralisation": 0.8
    }
  },
  ...
]
```

### Epoch

#### get_epoch_info
Get the epoch information, all epochs if no epoch specified<br>
Parameters: Epoch (optional)<br>
Returns: The list of epoch info dictionaries<br>
Example:<br>
`epoch_info = get_epoch_info(379)`<br>
Example response:
```json
[
  {
    "epoch_no": 379,
    "out_sum": "64893877572584948",
    "fees": "109846112870",
    "tx_count": 338483,
    "blk_count": 20947,
    "start_time": 1669931091,
    "end_time": 1670363091,
    "first_block_time": 1669931129,
    "last_block_time": 1670363027,
    "active_stake": "25058875481572529",
    "total_rewards": "12661794573764",
    "avg_blk_reward": "604468161"
  }
]
```

#### get_epoch_params
Get the protocol parameters for specific epoch, returns information about all epochs if no epoch specified<br>
Parameters: Epoch (optional)<br>
Returns: The list of epoch protocol parameters dictionaries<br>
Example:<br>
`epoch_params = get_epoch_params(380)`<br>
Example response:
```json
[
  {
    "epoch_no": 380,
    "min_fee_a": 44,
    "min_fee_b": 155381,
    "max_block_size": 90112,
    "max_tx_size": 16384,
    "max_bh_size": 1100,
    "key_deposit": "2000000",
    "pool_deposit": "500000000",
    "max_epoch": 18,
    "optimal_pool_count": 500,
    "influence": 0.3,
    "monetary_expand_rate": 0.003,
    "treasury_growth_rate": 0.2,
    "decentralisation": 0,
    "extra_entropy": null,
    "protocol_major": 7,
    "protocol_minor": 0,
    "min_utxo_value": "4310",
    "min_pool_cost": "340000000",
    "nonce": "3950677ef48bb212ad335f253ad1998be4e9fe4ae2a26d402607850461398125",
    "block_hash": "50a41a4841185a4f01def36c35f565ee2e1c27ee0e3ddb56885c244e49b24bf4",
    "cost_models": "{\"PlutusV1\": {\"bData-cpu-arguments\": 1000, \"iData-cpu-arguments\": 1000, \"trace-cpu-arguments\": 212342, \"mkCons-cpu-arguments\": 65493, \"fstPair-cpu-arguments\": 80436, \"mapData-cpu-arguments\": 64832, \"sndPair-cpu-arguments\": 85931, \"unBData-cpu-arguments\": 31220, \"unIData-cpu-arguments\": 43357, \"bData-memory-arguments\": 32, \"cekLamCost-exBudgetCPU\": 23000, \"cekVarCost-exBudgetCPU\": 23000, \"headList-cpu-arguments\": 43249, \"iData-memory-arguments\": 32, \"listData-cpu-arguments\": 52467, \"nullList-cpu-arguments\": 60091, \"tailList-cpu-arguments\": 41182, \"trace-memory-arguments\": 32, \"mkCons-memory-arguments\": 32, \"mkNilData-cpu-arguments\": 22558, \"unMapData-cpu-arguments\": 38314, \"cekApplyCost-exBudgetCPU\": 23000, \"cekConstCost-exBudgetCPU\": 23000, \"cekDelayCost-exBudgetCPU\": 23000, \"cekForceCost-exBudgetCPU\": 23000, \"chooseData-cpu-arguments\": 19537, \"chooseList-cpu-arguments\": 175354, \"chooseUnit-cpu-arguments\": 46417, \"constrData-cpu-arguments\": 89141, \"fstPair-memory-arguments\": 32, \"ifThenElse-cpu-arguments\": 80556, \"mapData-memory-arguments\": 32, \"mkPairData-cpu-arguments\": 76511, \"sndPair-memory-arguments\": 32, \"unBData-memory-arguments\": 32, \"unIData-memory-arguments\": 32, \"unListData-cpu-arguments\": 32247, \"cekLamCost-exBudgetMemory\": 100, \"cekVarCost-exBudgetMemory\": 100, \"headList-memory-arguments\": 32, \"listData-memory-arguments\": 32, \"nullList-memory-arguments\": 32, \"sha2_256-memory-arguments\": 4, \"sha3_256-memory-arguments\": 4, \"tailList-memory-arguments\": 32, \"cekBuiltinCost-exBudgetCPU\": 23000, \"cekStartupCost-exBudgetCPU\": 100, \"mkNilData-memory-arguments\": 32, \"unConstrData-cpu-arguments\": 32696, \"unMapData-memory-arguments\": 32, \"cekApplyCost-exBudgetMemory\": 100, \"cekConstCost-exBudgetMemory\": 100, \"cekDelayCost-exBudgetMemory\": 100, \"cekForceCost-exBudgetMemory\": 100, \"chooseData-memory-arguments\": 32, \"chooseList-memory-arguments\": 32, \"chooseUnit-memory-arguments\": 4, \"constrData-memory-arguments\": 32, \"equalsData-memory-arguments\": 1, \"ifThenElse-memory-arguments\": 1, \"mkNilPairData-cpu-arguments\": 16563, \"mkPairData-memory-arguments\": 32, \"unListData-memory-arguments\": 32, \"blake2b_256-memory-arguments\": 4, \"sha2_256-cpu-arguments-slope\": 30482, \"sha3_256-cpu-arguments-slope\": 82523, \"cekBuiltinCost-exBudgetMemory\": 100, \"cekStartupCost-exBudgetMemory\": 100, \"equalsString-memory-arguments\": 1, \"indexByteString-cpu-arguments\": 57667, \"unConstrData-memory-arguments\": 32, \"addInteger-cpu-arguments-slope\": 812, \"decodeUtf8-cpu-arguments-slope\": 14068, \"encodeUtf8-cpu-arguments-slope\": 28662, \"equalsData-cpu-arguments-slope\": 12586, \"equalsInteger-memory-arguments\": 1, \"mkNilPairData-memory-arguments\": 32, \"blake2b_256-cpu-arguments-slope\": 10475, \"appendString-cpu-arguments-slope\": 24177, \"equalsString-cpu-arguments-slope\": 52998, \"indexByteString-memory-arguments\": 4, \"lengthOfByteString-cpu-arguments\": 1000, \"lessThanInteger-memory-arguments\": 1, \"sha2_256-cpu-arguments-intercept\": 806990, \"sha3_256-cpu-arguments-intercept\": 1927926, \"addInteger-memory-arguments-slope\": 1, \"decodeUtf8-memory-arguments-slope\": 2, \"encodeUtf8-memory-arguments-slope\": 2, \"equalsByteString-memory-arguments\": 1, \"equalsInteger-cpu-arguments-slope\": 421, \"modInteger-cpu-arguments-constant\": 196500, \"modInteger-memory-arguments-slope\": 1, \"addInteger-cpu-arguments-intercept\": 205665, \"consByteString-cpu-arguments-slope\": 511, \"decodeUtf8-cpu-arguments-intercept\": 497525, \"encodeUtf8-cpu-arguments-intercept\": 1000, \"equalsData-cpu-arguments-intercept\": 1060367, \"appendString-memory-arguments-slope\": 1, \"blake2b_256-cpu-arguments-intercept\": 117366, \"equalsString-cpu-arguments-constant\": 187000, \"lengthOfByteString-memory-arguments\": 10, \"lessThanByteString-memory-arguments\": 1, \"lessThanInteger-cpu-arguments-slope\": 511, \"modInteger-memory-arguments-minimum\": 1, \"multiplyInteger-cpu-arguments-slope\": 11687, \"sliceByteString-cpu-arguments-slope\": 0, \"subtractInteger-cpu-arguments-slope\": 812, \"appendByteString-cpu-arguments-slope\": 571, \"appendString-cpu-arguments-intercept\": 1000, \"divideInteger-cpu-arguments-constant\": 196500, \"divideInteger-memory-arguments-slope\": 1, \"equalsByteString-cpu-arguments-slope\": 62, \"equalsString-cpu-arguments-intercept\": 1000, \"addInteger-memory-arguments-intercept\": 1, \"consByteString-memory-arguments-slope\": 1, \"decodeUtf8-memory-arguments-intercept\": 4, \"encodeUtf8-memory-arguments-intercept\": 4, \"equalsInteger-cpu-arguments-intercept\": 208512, \"modInteger-memory-arguments-intercept\": 0, \"consByteString-cpu-arguments-intercept\": 221973, \"divideInteger-memory-arguments-minimum\": 1, \"lessThanByteString-cpu-arguments-slope\": 156, \"lessThanEqualsInteger-memory-arguments\": 1, \"multiplyInteger-memory-arguments-slope\": 1, \"quotientInteger-cpu-arguments-constant\": 196500, \"quotientInteger-memory-arguments-slope\": 1, \"sliceByteString-memory-arguments-slope\": 0, \"subtractInteger-memory-arguments-slope\": 1, \"appendByteString-memory-arguments-slope\": 1, \"appendString-memory-arguments-intercept\": 4, \"equalsByteString-cpu-arguments-constant\": 245000, \"lessThanInteger-cpu-arguments-intercept\": 208896, \"multiplyInteger-cpu-arguments-intercept\": 69522, \"remainderInteger-cpu-arguments-constant\": 196500, \"remainderInteger-memory-arguments-slope\": 1, \"sliceByteString-cpu-arguments-intercept\": 265318, \"subtractInteger-cpu-arguments-intercept\": 205665, \"verifyEd25519Signature-memory-arguments\": 10, \"appendByteString-cpu-arguments-intercept\": 1000, \"divideInteger-memory-arguments-intercept\": 0, \"equalsByteString-cpu-arguments-intercept\": 216773, \"quotientInteger-memory-arguments-minimum\": 1, \"consByteString-memory-arguments-intercept\": 0, \"lessThanEqualsByteString-memory-arguments\": 1, \"lessThanEqualsInteger-cpu-arguments-slope\": 473, \"remainderInteger-memory-arguments-minimum\": 1, \"lessThanByteString-cpu-arguments-intercept\": 197145, \"multiplyInteger-memory-arguments-intercept\": 0, \"quotientInteger-memory-arguments-intercept\": 0, \"sliceByteString-memory-arguments-intercept\": 4, \"subtractInteger-memory-arguments-intercept\": 1, \"verifyEd25519Signature-cpu-arguments-slope\": 1021, \"appendByteString-memory-arguments-intercept\": 0, \"remainderInteger-memory-arguments-intercept\": 0, \"lessThanEqualsByteString-cpu-arguments-slope\": 156, \"lessThanEqualsInteger-cpu-arguments-intercept\": 204924, \"modInteger-cpu-arguments-model-arguments-slope\": 220, \"verifyEd25519Signature-cpu-arguments-intercept\": 9462713, \"lessThanEqualsByteString-cpu-arguments-intercept\": 197145, \"divideInteger-cpu-arguments-model-arguments-slope\": 220, \"modInteger-cpu-arguments-model-arguments-intercept\": 453240, \"quotientInteger-cpu-arguments-model-arguments-slope\": 220, \"remainderInteger-cpu-arguments-model-arguments-slope\": 220, \"divideInteger-cpu-arguments-model-arguments-intercept\": 453240, \"quotientInteger-cpu-arguments-model-arguments-intercept\": 453240, \"remainderInteger-cpu-arguments-model-arguments-intercept\": 453240}, \"PlutusV2\": {\"bData-cpu-arguments\": 1000, \"iData-cpu-arguments\": 1000, \"trace-cpu-arguments\": 212342, \"mkCons-cpu-arguments\": 65493, \"fstPair-cpu-arguments\": 80436, \"mapData-cpu-arguments\": 64832, \"sndPair-cpu-arguments\": 85931, \"unBData-cpu-arguments\": 31220, \"unIData-cpu-arguments\": 43357, \"bData-memory-arguments\": 32, \"cekLamCost-exBudgetCPU\": 23000, \"cekVarCost-exBudgetCPU\": 23000, \"headList-cpu-arguments\": 43249, \"iData-memory-arguments\": 32, \"listData-cpu-arguments\": 52467, \"nullList-cpu-arguments\": 60091, \"tailList-cpu-arguments\": 41182, \"trace-memory-arguments\": 32, \"mkCons-memory-arguments\": 32, \"mkNilData-cpu-arguments\": 22558, \"unMapData-cpu-arguments\": 38314, \"cekApplyCost-exBudgetCPU\": 23000, \"cekConstCost-exBudgetCPU\": 23000, \"cekDelayCost-exBudgetCPU\": 23000, \"cekForceCost-exBudgetCPU\": 23000, \"chooseData-cpu-arguments\": 19537, \"chooseList-cpu-arguments\": 175354, \"chooseUnit-cpu-arguments\": 46417, \"constrData-cpu-arguments\": 89141, \"fstPair-memory-arguments\": 32, \"ifThenElse-cpu-arguments\": 80556, \"mapData-memory-arguments\": 32, \"mkPairData-cpu-arguments\": 76511, \"sndPair-memory-arguments\": 32, \"unBData-memory-arguments\": 32, \"unIData-memory-arguments\": 32, \"unListData-cpu-arguments\": 32247, \"cekLamCost-exBudgetMemory\": 100, \"cekVarCost-exBudgetMemory\": 100, \"headList-memory-arguments\": 32, \"listData-memory-arguments\": 32, \"nullList-memory-arguments\": 32, \"sha2_256-memory-arguments\": 4, \"sha3_256-memory-arguments\": 4, \"tailList-memory-arguments\": 32, \"cekBuiltinCost-exBudgetCPU\": 23000, \"cekStartupCost-exBudgetCPU\": 100, \"mkNilData-memory-arguments\": 32, \"unConstrData-cpu-arguments\": 32696, \"unMapData-memory-arguments\": 32, \"cekApplyCost-exBudgetMemory\": 100, \"cekConstCost-exBudgetMemory\": 100, \"cekDelayCost-exBudgetMemory\": 100, \"cekForceCost-exBudgetMemory\": 100, \"chooseData-memory-arguments\": 32, \"chooseList-memory-arguments\": 32, \"chooseUnit-memory-arguments\": 4, \"constrData-memory-arguments\": 32, \"equalsData-memory-arguments\": 1, \"ifThenElse-memory-arguments\": 1, \"mkNilPairData-cpu-arguments\": 16563, \"mkPairData-memory-arguments\": 32, \"unListData-memory-arguments\": 32, \"blake2b_256-memory-arguments\": 4, \"sha2_256-cpu-arguments-slope\": 30482, \"sha3_256-cpu-arguments-slope\": 82523, \"cekBuiltinCost-exBudgetMemory\": 100, \"cekStartupCost-exBudgetMemory\": 100, \"equalsString-memory-arguments\": 1, \"indexByteString-cpu-arguments\": 57667, \"unConstrData-memory-arguments\": 32, \"addInteger-cpu-arguments-slope\": 812, \"decodeUtf8-cpu-arguments-slope\": 14068, \"encodeUtf8-cpu-arguments-slope\": 28662, \"equalsData-cpu-arguments-slope\": 12586, \"equalsInteger-memory-arguments\": 1, \"mkNilPairData-memory-arguments\": 32, \"blake2b_256-cpu-arguments-slope\": 10475, \"appendString-cpu-arguments-slope\": 24177, \"equalsString-cpu-arguments-slope\": 52998, \"indexByteString-memory-arguments\": 4, \"lengthOfByteString-cpu-arguments\": 1000, \"lessThanInteger-memory-arguments\": 1, \"sha2_256-cpu-arguments-intercept\": 806990, \"sha3_256-cpu-arguments-intercept\": 1927926, \"addInteger-memory-arguments-slope\": 1, \"decodeUtf8-memory-arguments-slope\": 2, \"encodeUtf8-memory-arguments-slope\": 2, \"equalsByteString-memory-arguments\": 1, \"equalsInteger-cpu-arguments-slope\": 421, \"modInteger-cpu-arguments-constant\": 196500, \"modInteger-memory-arguments-slope\": 1, \"serialiseData-cpu-arguments-slope\": 392670, \"addInteger-cpu-arguments-intercept\": 205665, \"consByteString-cpu-arguments-slope\": 511, \"decodeUtf8-cpu-arguments-intercept\": 497525, \"encodeUtf8-cpu-arguments-intercept\": 1000, \"equalsData-cpu-arguments-intercept\": 1060367, \"appendString-memory-arguments-slope\": 1, \"blake2b_256-cpu-arguments-intercept\": 117366, \"equalsString-cpu-arguments-constant\": 187000, \"lengthOfByteString-memory-arguments\": 10, \"lessThanByteString-memory-arguments\": 1, \"lessThanInteger-cpu-arguments-slope\": 511, \"modInteger-memory-arguments-minimum\": 1, \"multiplyInteger-cpu-arguments-slope\": 11687, \"sliceByteString-cpu-arguments-slope\": 0, \"subtractInteger-cpu-arguments-slope\": 812, \"appendByteString-cpu-arguments-slope\": 571, \"appendString-cpu-arguments-intercept\": 1000, \"divideInteger-cpu-arguments-constant\": 196500, \"divideInteger-memory-arguments-slope\": 1, \"equalsByteString-cpu-arguments-slope\": 62, \"equalsString-cpu-arguments-intercept\": 1000, \"serialiseData-memory-arguments-slope\": 2, \"addInteger-memory-arguments-intercept\": 1, \"consByteString-memory-arguments-slope\": 1, \"decodeUtf8-memory-arguments-intercept\": 4, \"encodeUtf8-memory-arguments-intercept\": 4, \"equalsInteger-cpu-arguments-intercept\": 208512, \"modInteger-memory-arguments-intercept\": 0, \"serialiseData-cpu-arguments-intercept\": 1159724, \"consByteString-cpu-arguments-intercept\": 221973, \"divideInteger-memory-arguments-minimum\": 1, \"lessThanByteString-cpu-arguments-slope\": 156, \"lessThanEqualsInteger-memory-arguments\": 1, \"multiplyInteger-memory-arguments-slope\": 1, \"quotientInteger-cpu-arguments-constant\": 196500, \"quotientInteger-memory-arguments-slope\": 1, \"sliceByteString-memory-arguments-slope\": 0, \"subtractInteger-memory-arguments-slope\": 1, \"appendByteString-memory-arguments-slope\": 1, \"appendString-memory-arguments-intercept\": 4, \"equalsByteString-cpu-arguments-constant\": 245000, \"lessThanInteger-cpu-arguments-intercept\": 208896, \"multiplyInteger-cpu-arguments-intercept\": 69522, \"remainderInteger-cpu-arguments-constant\": 196500, \"remainderInteger-memory-arguments-slope\": 1, \"sliceByteString-cpu-arguments-intercept\": 265318, \"subtractInteger-cpu-arguments-intercept\": 205665, \"verifyEd25519Signature-memory-arguments\": 10, \"appendByteString-cpu-arguments-intercept\": 1000, \"divideInteger-memory-arguments-intercept\": 0, \"equalsByteString-cpu-arguments-intercept\": 216773, \"quotientInteger-memory-arguments-minimum\": 1, \"serialiseData-memory-arguments-intercept\": 0, \"consByteString-memory-arguments-intercept\": 0, \"lessThanEqualsByteString-memory-arguments\": 1, \"lessThanEqualsInteger-cpu-arguments-slope\": 473, \"remainderInteger-memory-arguments-minimum\": 1, \"lessThanByteString-cpu-arguments-intercept\": 197145, \"multiplyInteger-memory-arguments-intercept\": 0, \"quotientInteger-memory-arguments-intercept\": 0, \"sliceByteString-memory-arguments-intercept\": 4, \"subtractInteger-memory-arguments-intercept\": 1, \"verifyEd25519Signature-cpu-arguments-slope\": 1021, \"appendByteString-memory-arguments-intercept\": 0, \"remainderInteger-memory-arguments-intercept\": 0, \"verifyEcdsaSecp256k1Signature-cpu-arguments\": 20000000000, \"lessThanEqualsByteString-cpu-arguments-slope\": 156, \"lessThanEqualsInteger-cpu-arguments-intercept\": 204924, \"modInteger-cpu-arguments-model-arguments-slope\": 220, \"verifyEcdsaSecp256k1Signature-memory-arguments\": 20000000000, \"verifyEd25519Signature-cpu-arguments-intercept\": 9462713, \"lessThanEqualsByteString-cpu-arguments-intercept\": 197145, \"verifySchnorrSecp256k1Signature-memory-arguments\": 20000000000, \"divideInteger-cpu-arguments-model-arguments-slope\": 220, \"modInteger-cpu-arguments-model-arguments-intercept\": 453240, \"quotientInteger-cpu-arguments-model-arguments-slope\": 220, \"verifySchnorrSecp256k1Signature-cpu-arguments-slope\": 0, \"remainderInteger-cpu-arguments-model-arguments-slope\": 220, \"divideInteger-cpu-arguments-model-arguments-intercept\": 453240, \"quotientInteger-cpu-arguments-model-arguments-intercept\": 453240, \"verifySchnorrSecp256k1Signature-cpu-arguments-intercept\": 20000000000, \"remainderInteger-cpu-arguments-model-arguments-intercept\": 453240}}",
    "price_mem": 0.0577,
    "price_step": 0.0000721,
    "max_tx_ex_mem": 14000000,
    "max_tx_ex_steps": 10000000000,
    "max_block_ex_mem": 62000000,
    "max_block_ex_steps": 40000000000,
    "max_val_size": 5000,
    "collateral_percent": 150,
    "max_collateral_inputs": 3,
    "coins_per_utxo_size": "4310"
  }
]
```

#### get_epoch_block_protocols
Get the information about block protocol distribution in epoch<br>
Parameters: Epoch (optional)<br>
Returns: The list of epoch protocol distribution dictionaries<br>
Example:<br>
`epoch_block_protocols = get_epoch_block_protocols(380)`<br>
Example response:
```json
[
  {
    "proto_major": 7,
    "proto_minor": 0,
    "blocks": 8930
  },
  {
    "proto_major": 8,
    "proto_minor": 0,
    "blocks": 12340
  }
]
```

### Block

#### get_blocks
Get summarised details about all blocks (paginated - latest first)<br>
Parameters: The maximum number of blocks to return<br>
Returns: The list of block dictionaries (the newest first)<br>
Example:<br>
`blocks = get_blocks(3)`<br>
Example response:
```json
[
  {
    "hash": "8e33bb588feff6414469779d724923064688615535280f8982c9981410cd06f6",
    "epoch_no": 381,
    "abs_slot": 79266935,
    "epoch_slot": 38135,
    "block_height": 8129401,
    "block_size": 49025,
    "block_time": 1670833226,
    "tx_count": 19,
    "vrf_key": "vrf_vk1pj8n7cv07gn4s83vnxgnh3l4m0uqunud2hfmn6d203v6gjvn6jfq9yanjy",
    "pool": "pool1qqq6qqa0hpzvumv5p87ynczfmdj557xuwlc3289ke42g72z7f74",
    "proto_major": 8,
    "proto_minor": 0,
    "op_cert_counter": 10
  },
  {
    "hash": "6464132c9227e39f2a9bca27d738a28d9cd64aba37f55277d75e7e8e0aa5d892",
    "epoch_no": 381,
    "abs_slot": 79266917,
    "epoch_slot": 38117,
    "block_height": 8129400,
    "block_size": 88807,
    "block_time": 1670833208,
    "tx_count": 52,
    "vrf_key": "vrf_vk1hnkdcm6y67amyfnhu4gv2n77496wxmnznke6fqdan53j20mc6jjq7q98e6",
    "pool": "pool1nhd907krga9dh69kf0jg4tl0764rravepy337gptvsknxyyx94k",
    "proto_major": 8,
    "proto_minor": 0,
    "op_cert_counter": 20
  },
  {
    "hash": "7ba6d760e576d3b078dedd931284e0f818306fd71bdba47a0fc6b8b9b7c22dbc",
    "epoch_no": 381,
    "abs_slot": 79266839,
    "epoch_slot": 38039,
    "block_height": 8129399,
    "block_size": 10031,
    "block_time": 1670833130,
    "tx_count": 7,
    "vrf_key": "vrf_vk1kchxdfjqfew7vt88e7l6q2eg3nylf5arahhp8pzfn5z2eyy0z4tsg7sr5k",
    "pool": "pool15yyxtkhz64p7a8cnax9l7u82s9t9hdhyxsa3tdm977qhgpnsuhq",
    "proto_major": 7,
    "proto_minor": 0,
    "op_cert_counter": 30
  }
]
```

#### get_block_info
Get detailed information about a specific block<br>
Parameters: Block hash as string (for one block) or list of block hashes (for multiple blocks)<br>
Returns: The list of block dictionaries<br>
Example:<br>
`block_info = get_block_info('8e33bb588feff6414469779d724923064688615535280f8982c9981410cd06f6')`<br>
Example response:
```json
[
  {
    "hash": "8e33bb588feff6414469779d724923064688615535280f8982c9981410cd06f6",
    "epoch_no": 381,
    "abs_slot": 79266935,
    "epoch_slot": 38135,
    "block_height": 8129401,
    "block_size": 49025,
    "block_time": 1670833226,
    "tx_count": 19,
    "vrf_key": "vrf_vk1pj8n7cv07gn4s83vnxgnh3l4m0uqunud2hfmn6d203v6gjvn6jfq9yanjy",
    "op_cert": "9dac36a4e413be97bcc4d34341023d3ee9d825e27a45beac739270f6e344d478",
    "op_cert_counter": 10,
    "pool": "pool1qqq6qqa0hpzvumv5p87ynczfmdj557xuwlc3289ke42g72z7f74",
    "proto_major": 8,
    "proto_minor": 0,
    "total_output": "45569728258134",
    "total_fees": "5966381",
    "num_confirmations": 10,
    "parent_hash": null,
    "child_hash": null
  }
]
```

#### get_block_txs
Get a list of all transactions included in provided blocks<br>
Parameters: Block(s) hash(es) as string (for one block) or list of block hashes (for multiple blocks)<br>
Returns: The list of transaction dictionaries by block<br>
Example:<br>
`block_txs = get_block_txs('8e33bb588feff6414469779d724923064688615535280f8982c9981410cd06f6')`<br>
Example response:
```json
[
  {
    "block_hash": "8e33bb588feff6414469779d724923064688615535280f8982c9981410cd06f6",
    "tx_hashes": [
      "d1c7496398b02cb2833c3e164947e1ec171819b7ec056fc6b798e2ee122af862",
      "6fe4152a34ee23ccdb5b42e9397ec1c960e51eb28d101b7a59645ce8299fa553",
      "2982bdebe8425c19a275416331cdb54d71409e9107e0add51784a37735fc2316",
      "bf685dde61d36b8acd259b2bd00a69a2e8359d2a69b75aa3a0eff9d38ca1f2ef",
      "291b5533227331999eca2e63934c1061e5f85993e77747a90d9901413d7bb937",
      "505057f2ce7e9cc2442c6dd2339e476e916f1d7b03888110c455082a808e47f5",
      "1b4cab1352b8f5b91f97a05c05244ad654282ece5b5f118a0302bc90c86e7476",
      "9f38998d3ef516f3150a1dc1f8a3f96ca8aa98636b63d835b4f480712d010474",
      "99f2aefba2a4a5a550aeed9d91d3adabe77a286ec45c345c7980a208364f76c6",
      "0eec38dc1d2d021f477a890d754e66c49fe74a9fd972793076587496c9850060",
      "a42ee1a5685ff6953464c32af6221b43732a8550d40f2b7f67f6d2250dfdcbb2",
      "63f99851ff566f801552aed538f8edd2eb4d20b9b66d475f2d51b075595443e7",
      "ecc46903435f89dde0e65865404a1c3a3af0ec78e08ff6e771e410539037f35e",
      "1515e444851c9c7d3abe85ff275c5fd5af8d4844da04f1472d343bcc27f7e58c",
      "12ad9fd5bb7482ee08de25d748288c41df4b05ac079d307a36b6159980fa4b03",
      "c99ed71da7c20d34ceba491c68e60a94c898db0c4b4360f54da09f7ae09370f0",
      "a061003549062114645dfd5d7a353189edb2b6d0f9049f8b1a52ee42d5397247",
      "57619d9198ac449cda755e255ed639d43c82a0e38ec001194f373a151d05a159",
      "6a4adc1e4ef496dc5fadb01641cc849633a13524ac63800a1e1c2e4e87238777"
    ]
  }
]
```

### Transactions

#### get_tx_info
Get detailed information about transaction(s)<br>
Parameters: Transaction(s) hash(es) as a string (for one transaction) or list (for multiple transactions)<br>
Returns: The list of transactions details dictionaries<br>
Example:<br>
`tx_info = get_tx_info('99f2aefba2a4a5a550aeed9d91d3adabe77a286ec45c345c7980a208364f76c6')`<br>
Example response:
```json
[
  {
    "tx_hash": "99f2aefba2a4a5a550aeed9d91d3adabe77a286ec45c345c7980a208364f76c6",
    "block_hash": "8e33bb588feff6414469779d724923064688615535280f8982c9981410cd06f6",
    "block_height": 8129401,
    "epoch_no": 381,
    "epoch_slot": 38135,
    "absolute_slot": 79266935,
    "tx_timestamp": 1670833226,
    "tx_block_index": 8,
    "tx_size": 436,
    "total_output": "4817999",
    "fee": "182001",
    "deposit": "0",
    "invalid_before": null,
    "invalid_after": null,
    "collateral_inputs": [],
    "collateral_output": null,
    "reference_inputs": [],
    "inputs": [
      {
        "value": "5000000",
        "tx_hash": "1d6776a3a1bed38f6705bc8c861c2a49d65423ecac9409f4a532a085901e29f8",
        "tx_index": 0,
        "asset_list": [
          {
            "quantity": "2",
            "policy_id": "27eee19588c997ca54d3137f64afe55a18dfcf9062fa83a724bf2357",
            "asset_name": "414952",
            "fingerprint": "asset1cl5pvxah2ckvdfax3uzsk57ffxw67m98da5v25"
          },
          {
            "quantity": "2",
            "policy_id": "27eee19588c997ca54d3137f64afe55a18dfcf9062fa83a724bf2357",
            "asset_name": "4541525448",
            "fingerprint": "asset1udwewa3sp34ukmeddhkwf8msqd6dq6frhy2j9s"
          }
        ],
        "datum_hash": null,
        "stake_addr": null,
        "inline_datum": null,
        "payment_addr": {
          "cred": "48edbef119f1330e0faa124f623054ab5e2e4464e9f6c9b8ebf0afaf",
          "bech32": "addr1v9ywm0h3r8cnxrs04gfy7c3s2j44utjyvn5ldjdca0c2ltccgqdes"
        },
        "reference_script": null
      }
    ],
    "outputs": [
      {
        "value": "4817999",
        "tx_hash": "99f2aefba2a4a5a550aeed9d91d3adabe77a286ec45c345c7980a208364f76c6",
        "tx_index": 0,
        "asset_list": [
          {
            "quantity": "1",
            "policy_id": "27eee19588c997ca54d3137f64afe55a18dfcf9062fa83a724bf2357",
            "asset_name": "414952",
            "fingerprint": "asset1cl5pvxah2ckvdfax3uzsk57ffxw67m98da5v25"
          }
        ],
        "datum_hash": null,
        "stake_addr": "stake1uxfymrvj2zzkdt7fdz3scj5mr3tc5qkpau8au253heglzmqjatts0",
        "inline_datum": null,
        "payment_addr": {
          "cred": "28540e24fadfc844d2f2fae09933d631de1baae05cc7d767da292cdf",
          "bech32": "addr1qy59gr3ylt0us3xj7tawpxfn6ccauxa2upwv04m8mg5jehujfkxey5y9v6huj69rp39fk8zh3gpvrmc0mc4fr0j379kqp865ns"
        },
        "reference_script": null
      }
    ],
    "withdrawals": [],
    "assets_minted": [
      {
        "quantity": "-1",
        "policy_id": "27eee19588c997ca54d3137f64afe55a18dfcf9062fa83a724bf2357",
        "asset_name": "414952",
        "fingerprint": "asset1cl5pvxah2ckvdfax3uzsk57ffxw67m98da5v25"
      },
      {
        "quantity": "-2",
        "policy_id": "27eee19588c997ca54d3137f64afe55a18dfcf9062fa83a724bf2357",
        "asset_name": "4541525448",
        "fingerprint": "asset1udwewa3sp34ukmeddhkwf8msqd6dq6frhy2j9s"
      }
    ],
    "metadata": null,
    "certificates": [],
    "native_scripts": [],
    "plutus_contracts": []
  }
]
```

#### get_tx_utxos
Get UTxO set (inputs/outputs) of transactions<br>
Parameters: Transaction(s) hash(es) as a string (for one transaction) or list (for multiple transactions)<br>
Returns: The list of transactions UTxOs dictionaries<br>
Example:<br>
`tx_utxos = get_tx_utxos('bf685dde61d36b8acd259b2bd00a69a2e8359d2a69b75aa3a0eff9d38ca1f2ef')`<br>
Example response:
```json
[
  {
    "tx_hash": "bf685dde61d36b8acd259b2bd00a69a2e8359d2a69b75aa3a0eff9d38ca1f2ef",
    "inputs": [
      {
        "payment_addr": {
          "bech32": "addr1q8wv876ptu0qhujmh2awdcnpcc0ctgdz8e8qvv29k8hucwft99azzjfn9l2658p483uljfdd00ef5rzg58y5km6gj9jqcp0ws7",
          "cred": "dcc3fb415f1e0bf25bbabae6e261c61f85a1a23e4e063145b1efcc39"
        },
        "stake_addr": "stake1uy4jj73pfyejl4d2rs6nc70eykkhhu56p3y2rj2tdayfzeqnjyh0j",
        "tx_hash": "2534b92a1d04ef39f9915bef8d7c5246cc4db880ac01f3499fe9aa83ac155a19",
        "tx_index": 2,
        "value": "14602840",
        "asset_list": []
      },
      {
        "payment_addr": {
          "bech32": "addr1zxgx3far7qygq0k6epa0zcvcvrevmn0ypsnfsue94nsn3tvpw288a4x0xf8pxgcntelxmyclq83s0ykeehchz2wtspks905plm",
          "cred": "9068a7a3f008803edac87af1619860f2cdcde40c26987325ace138ad"
        },
        "stake_addr": "stake1uxqh9rn76n8nynsnyvf4ulndjv0srcc8jtvumut3989cqmgjt49h6",
        "tx_hash": "2534b92a1d04ef39f9915bef8d7c5246cc4db880ac01f3499fe9aa83ac155a19",
        "tx_index": 0,
        "value": "1327480",
        "asset_list": [
          {
            "policy_id": "11ebbfbfd62985cbae7330b95488b9dcf17ecb5e728442031362ad81",
            "asset_name": "48756e677279436f772333313835",
            "fingerprint": "asset1kgzw0q7pt42zeerkn9sctpz3s5gan3xfrjpsgd",
            "quantity": "1"
          }
        ]
      }
    ],
    "outputs": [
      {
        "payment_addr": {
          "bech32": "addr1q8wv876ptu0qhujmh2awdcnpcc0ctgdz8e8qvv29k8hucwft99azzjfn9l2658p483uljfdd00ef5rzg58y5km6gj9jqcp0ws7",
          "cred": "dcc3fb415f1e0bf25bbabae6e261c61f85a1a23e4e063145b1efcc39"
        },
        "stake_addr": "stake1uy4jj73pfyejl4d2rs6nc70eykkhhu56p3y2rj2tdayfzeqnjyh0j",
        "tx_hash": "bf685dde61d36b8acd259b2bd00a69a2e8359d2a69b75aa3a0eff9d38ca1f2ef",
        "tx_index": 0,
        "value": "1180940",
        "asset_list": [
          {
            "policy_id": "11ebbfbfd62985cbae7330b95488b9dcf17ecb5e728442031362ad81",
            "asset_name": "48756e677279436f772333313835",
            "fingerprint": "asset1kgzw0q7pt42zeerkn9sctpz3s5gan3xfrjpsgd",
            "quantity": "1"
          }
        ]
      },
      {
        "payment_addr": {
          "bech32": "addr1q8wv876ptu0qhujmh2awdcnpcc0ctgdz8e8qvv29k8hucwft99azzjfn9l2658p483uljfdd00ef5rzg58y5km6gj9jqcp0ws7",
          "cred": "dcc3fb415f1e0bf25bbabae6e261c61f85a1a23e4e063145b1efcc39"
        },
        "stake_addr": "stake1uy4jj73pfyejl4d2rs6nc70eykkhhu56p3y2rj2tdayfzeqnjyh0j",
        "tx_hash": "bf685dde61d36b8acd259b2bd00a69a2e8359d2a69b75aa3a0eff9d38ca1f2ef",
        "tx_index": 1,
        "value": "14481686",
        "asset_list": []
      }
    ]
  }
]
```

#### get_tx_metadata
Get metadata information (if any) for given transaction(s)<br>
Parameters: Transaction(s) hash(es) as a string (for one transaction) or list (for multiple transactions)<br>
Returns: The list of transactions metadata dictionaries<br>
Example:<br>
`tx_metadata = get_tx_metadata('291b5533227331999eca2e63934c1061e5f85993e77747a90d9901413d7bb937')`<br>
Example response:
```json
[
  {
    "tx_hash": "291b5533227331999eca2e63934c1061e5f85993e77747a90d9901413d7bb937",
    "metadata": {
      "0": "d8799f581c078075595cc992a8d99eaad00a118e59303f1dae095601a05dec15",
      "1": "9a9fd8799fd8799fd8799f581c07279c6cb6238c73c6ef7429894d7906a5b326",
      "2": "39faa311af8f56f884ffd87a80ffa140d8799f00a1401a069db9c0ffffd8799f",
      "3": "d8799fd8799f581c70e60f3b5ea7153e0acc7a803e4401d44b8ed1bae1c7baaa",
      "4": "d1a62a72ffd8799fd8799fd8799f581c1e78aae7c90cc36d624f7b3bb6d86b52",
      "5": "696dc84e490f343eba89005fffffffffa140d8799f00a1401a00a95f60ffffd8",
      "6": "799fd8799fd8799f581c078075595cc992a8d99eaad00a118e59303f1dae0956",
      "7": "01a05dec159affd8799fd8799fd8799f581c6921c483c2ba3451072c5f90058d",
      "8": "c40c7b35af88238dd105f82570d2ffffffffa140d8799f00a1401a19cd87a0ff",
      "9": "ffffff",
      "30": "4"
    }
  }
]
```

#### get_tx_metalabels
Get a list of all transaction metadata labels<br>
Parameters: none<br>
Returns: The list of transaction metadata labels dictionaries<br>
Example:<br>
`tx_metalabels = get_tx_metalabels()`<br>
Example response:
```json
[
  {
    "key": "0"
  },
  {
    "key": "1"
  },
  {
    "key": "2"
  },
  {
    "key": "3"
  },
  {
    "key": "4"
  },
  {
    "key": "5"
  },
  ...
  {
    "key": "1657732524678"
  },
  {
    "key": "1657905239358"
  }
]
```

#### submit_tx
Submit an already serialized transaction to the network<br>
Parameters: Transaction in cbor format<br>
Returns: Transaction hash<br>
Example:<br>
`response = submit_tx(tx)`<br>
Example response:
```
0eec38dc1d2d021f477a890d754e66c49fe74a9fd972793076587496c9850060
```

#### get_tx_status
Get the number of block confirmations for a given transaction hash list<br>
Parameters: Transaction(s) hash(es) as a string (for one transaction) or list (for multiple transactions)<br>
Returns: The list of transactions block confirmations dictionaries<br>
Example:<br>
`tx_status = get_tx_status('0eec38dc1d2d021f477a890d754e66c49fe74a9fd972793076587496c9850060')`<br>
Example response:
```json
[
  {
    "tx_hash": "0eec38dc1d2d021f477a890d754e66c49fe74a9fd972793076587496c9850060",
    "num_confirmations": 228
  }
]
```

### Address

#### get_address_info
Get the transaction hash list of input address array, optionally filtering after specified block height (inclusive)<br>
Parameters: Payment address(es) as string (for one address) or list (for multiple addresses)<br>
Returns: The list of transactions dictionaries<br>
Example:<br>
`address_info = get_address_info('addr1q8wv876ptu0qhujmh2awdcnpcc0ctgdz8e8qvv29k8hucwft99azzjfn9l2658p483uljfdd00ef5rzg58y5km6gj9jqcp0ws7')`<br>
Example response:
```json
[
  {
    "address": "addr1q8wv876ptu0qhujmh2awdcnpcc0ctgdz8e8qvv29k8hucwft99azzjfn9l2658p483uljfdd00ef5rzg58y5km6gj9jqcp0ws7",
    "balance": "15418617",
    "stake_address": "stake1uy4jj73pfyejl4d2rs6nc70eykkhhu56p3y2rj2tdayfzeqnjyh0j",
    "script_address": false,
    "utxo_set": [
      {
        "tx_hash": "c626fe027d09db2b6c63ba67e3638911ff70e3b691a7e5c03e75c0d3a168c973",
        "tx_index": 1,
        "block_height": 8129403,
        "block_time": 1670833300,
        "value": "15418617",
        "datum_hash": null,
        "inline_datum": null,
        "reference_script": null,
        "asset_list": []
      }
    ]
  }
]
```

#### get_address_txs
Get the transaction hash list of input address array, optionally filtering after specified block height (inclusive)<br>
Parameters: Payment address(es) as string (for one address) or list (for multiple addresses)<br>
Returns: The list of transactions dictionaries<br>
Example:<br>
`address_txs = get_address_txs('addr1q8wv876ptu0qhujmh2awdcnpcc0ctgdz8e8qvv29k8hucwft99azzjfn9l2658p483uljfdd00ef5rzg58y5km6gj9jqcp0ws7')`<br>
Example response:
```json
[
  {
    "tx_hash": "c626fe027d09db2b6c63ba67e3638911ff70e3b691a7e5c03e75c0d3a168c973",
    "epoch_no": 381,
    "block_height": 8129403,
    "block_time": 1670833300
  },
  {
    "tx_hash": "bf685dde61d36b8acd259b2bd00a69a2e8359d2a69b75aa3a0eff9d38ca1f2ef",
    "epoch_no": 381,
    "block_height": 8129401,
    "block_time": 1670833226
  },
  {
    "tx_hash": "2534b92a1d04ef39f9915bef8d7c5246cc4db880ac01f3499fe9aa83ac155a19",
    "epoch_no": 380,
    "block_height": 8127226,
    "block_time": 1670787767
  },
  ...
  {
    "tx_hash": "3c16d642fc92012a8808446b29fe89028a2bc37508048a9eb465265d30a24386",
    "epoch_no": 373,
    "block_height": 7971352,
    "block_time": 1667570778
  }
]
```

#### get_credential_utxos
Get a list of UTxO against input payment credential array including their balances<br>
Parameters: Payment credential(s) as string (for one credential) or list (for multiple credentials)<br>
Returns: The list of UTxO against input payment credential array including their balances<br>
Example:<br>
`credential_utxos = get_credential_utxos('0c35748e147183cd784875e78a5b372fa6975e9ac6406d6015c09bac')`<br>
Example response:<br>
```json
[
  {
    "tx_hash": "8e9b85284f92ad85416d4fb0a3ff5d3bbd9b57c4a4d97a8d39dc99316eace0cf",
    "tx_index": 0,
    "value": "5000000"
  },
  {
    "tx_hash": "e7333c01d3c2887767aca13e5c74fb858fbf0119cd90d944869ee72b8b81f523",
    "tx_index": 1,
    "value": "20432286"
  },
  {
    "tx_hash": "ecfbbc335ec203b10ee65faddf06fb0ceac27c36ef3a76047fbf820f6e9ed7f2",
    "tx_index": 2,
    "value": "2301540"
  },
  {
    "tx_hash": "b70a9107a38e776c0b1d94a1578c393a1ce01ea8e28ed56c5c724a2639e31bfe",
    "tx_index": 2,
    "value": "1150770"
  },
  {
    "tx_hash": "1107afdada22f259aa798de57ca3839e212e977467628c85315326917a13dd3b",
    "tx_index": 2,
    "value": "1150770"
  },
  ...
  {
    "tx_hash": "b9d519ff9309dd78a7e8031aef2fa6b21358478efed5f0bdf234fa10c83eede7",
    "tx_index": 1,
    "value": "137666866"
  }
]
```

#### get_address_assets
Get the list of all the assets (policy, name and quantity) for given addresses<br>
Parameters: Payment address(es) as string (for one address) or list (for multiple addresses)<br>
Returns: The list of assets dictionaries by address<br>
Example:<br>
`address_assets = get_address_assets('addr1qywp2795uk4uusknpseu3fcwy8ew57dnuaeutnxaa5j6ulp4u2anham4xet066yjc6xjxcymujvvwlfhj8k8gxfl2nvs73rvzh')`<br>
Example response:
```json
[
  {
    "address": "addr1qywp2795uk4uusknpseu3fcwy8ew57dnuaeutnxaa5j6ulp4u2anham4xet066yjc6xjxcymujvvwlfhj8k8gxfl2nvs73rvzh",
    "asset_list": [
      {
        "policy_id": "07697e6ca1e21777ac76f26d0779c53f7d08e47b9e32d23bd8fed9cd",
        "asset_name": "4379626572696130363936",
        "fingerprint": "asset1hf3u704jz0ranfa2ygnq4028ht4vgqz8gsgw70",
        "quantity": "1"
      },
      {
        "policy_id": "14a95b2a4a863c8074d6a78a6a445150223e867999a90295dc1d0cf6",
        "asset_name": "50726f6a65637456656e757330303536",
        "fingerprint": "asset1pdz0dvugfezf6evgyvvyl5zda8mhdfhef8d3fd",
        "quantity": "1"
      },
      ...
      {
        "policy_id": "ffff5571ecec795284f04ad6e6852ed2d46d924535ed68ad97fa1e70",
        "asset_name": "634e4654636f6e486f70706572363935",
        "fingerprint": "asset1dcn7mx0ccelvmweef6wjcuhur9a2hpg8des4pl",
        "quantity": "1"
      }
    ]
  }
]
```

#### get_credential_txs
Get the transaction hash list of input payment credential array, optionally filtering after specified block height (inclusive)<br>
Parameters: Credential(s) as string (for one credential) or list (for multiple credentials)<br>
Returns: The list of address information dictionaries<br>
Example:<br>
`credential_txs = get_credential_txs('dcc3fb415f1e0bf25bbabae6e261c61f85a1a23e4e063145b1efcc39')`<br>
Example response:
```json
[
  {
    "tx_hash": "c626fe027d09db2b6c63ba67e3638911ff70e3b691a7e5c03e75c0d3a168c973",
    "epoch_no": 381,
    "block_height": 8129403,
    "block_time": 1670833300
  },
  {
    "tx_hash": "bf685dde61d36b8acd259b2bd00a69a2e8359d2a69b75aa3a0eff9d38ca1f2ef",
    "epoch_no": 381,
    "block_height": 8129401,
    "block_time": 1670833226
  },
  ...
  {
    "tx_hash": "3c16d642fc92012a8808446b29fe89028a2bc37508048a9eb465265d30a24386",
    "epoch_no": 373,
    "block_height": 7971352,
    "block_time": 1667570778
  }
]
```

### Asset

#### get_asset_list
Get the list of all native assets (paginated)<br>
Parameters:<br>
Asset Policy (optional), default: all policies<br>
The offset (optional) to start from, default 0<br>
The maximum number of accounts to return (optional), default 0 (no limit)<br>
Returns: The list of assets dictionaries by policy<br>
Example:<br>
`asset_list = get_asset_list()`<br>
Example response:
```json
[
  {
    "policy_id": "00000002df633853f6a47465c9496721d2d5b1291b8398016c0e87ae",
    "asset_name": "6e7574636f696e",
    "fingerprint": "asset12h3p5l3nd5y26lr22am7y7ga3vxghkhf57zkhd"
  },
  {
    "policy_id": "000000adf8fcbdf03a5c154123aff674edf287fb13532a343b617fb2",
    "asset_name": "5853534e4654",
    "fingerprint": "asset1ke42k9ug86yr535qwkq5edlvfdvlpfuslrmfup"
  },
  ...
  {
    "policy_id": "00255c245861e1e15ef8aced64d44dd20682ee7c2bb42b7941e199dd",
    "asset_name": "43726565707942616c6c7a57316231303137",
    "fingerprint": "asset12dvnasghksl5k7w696nd5t692j6myexapwjh0d"
  },
  ...
]
```

#### get_asset_token_registry
Get a list of assets registered via token registry on github<br>
Parameters: none<br>
Returns: The list of assets registered via token registry on github<br>
Example:<br>
`asset_token_registry = get_asset_token_registry()`<br>
Example response:<br>
```json
[
  {
    "policy_id": "00000002df633853f6a47465c9496721d2d5b1291b8398016c0e87ae",
    "asset_name": "6e7574636f696e",
    "asset_name_ascii": "nutcoin",
    "ticker": "NUT",
    "description": "The legendary Nutcoin, the first native asset minted on Cardano.",
    "url": "https://fivebinaries.com/nutcoin",
    "decimals": 0,
    "logo": "iVBORw0KGgoAAAANSUhEUgAAAGQA....2rCPgau2EAAAAASUVORK5CYII="
  },
  {
    "policy_id": "00109530994ea381c0bfe0936c85ea01bfe2765c24ef6dad5740c33e",
    "asset_name": "486f646c657220436f616c6974696f6e20436f696e",
    "asset_name_ascii": "Hodler Coalition Coin",
    "ticker": "HODLR",
    "description": "Stake ₳DA with the Hodler Coalition. Save the World.",
    "url": "https://www.hodlerstaking.com/",
    "decimals": 4,
    "logo": "iVBORw0KGgoAAAANSUhEUgAAARAAA...4RtRz5t2G8zAAAAAElFTkSuQmCC"
  },
  {
    "policy_id": "0011fbab202151eca9e9ef7680569d9419d12e51e693cb05a2edd2ed",
    "asset_name": "4341524b",
    "asset_name_ascii": "Cardano Ark Token",
    "ticker": "CARK",
    "description": "Utility token for the Cardano Ark",
    "url": "https://www.cardanoark.com/",
    "decimals": 0,
    "logo": ""
  },
  ...
]
```

#### get_asset_addresses
Get the list of all addresses holding a given asset<br>
Parameters:<br>
Asset Policy<br>
Asset Name in hexadecimal format (optional), default: all policy assets<br>
Returns: List of dictionaries with the wallets holding the asset and the amount of assets per wallet<br>
Example:<br>
`asset_address_list = get_asset_address_list('07697e6ca1e21777ac76f26d0779c53f7d08e47b9e32d23bd8fed9cd', '4379626572696130363936')`<br>
Example response:
```json
[
  {
    "payment_address": "addr1qywp2795uk4uusknpseu3fcwy8ew57dnuaeutnxaa5j6ulp4u2anham4xet066yjc6xjxcymujvvwlfhj8k8gxfl2nvs73rvzh",
    "quantity": "1"
  }
]
```

#### get_asset_nft_address
Get the address where specified NFT currently reside on.<br>
Parameters:<br>
Asset Policy<br>
Asset Name in hexadecimal format<br>
Returns: The wallet address holding the NFT as a list of one dictionary<br>
Example:<br>
`asset_nft_address = get_asset_nft_address('07697e6ca1e21777ac76f26d0779c53f7d08e47b9e32d23bd8fed9cd', '4379626572696130363936')`<br>
Example response:
```json
[
  {
    "payment_address": "addr1qywp2795uk4uusknpseu3fcwy8ew57dnuaeutnxaa5j6ulp4u2anham4xet066yjc6xjxcymujvvwlfhj8k8gxfl2nvs73rvzh"
  }
]
```

#### get_asset_info
Get the information of an asset including first minting & token registry metadata<br>
Parameters:
Asset Policy<br>
Asset Name in hexadecimal format (optional), default: all policy assets<br>
Returns: List of dictionaries with the wallets holding the asset and the amount of assets per wallet<br>
Example:<br>
`asset_info = get_asset_info('07697e6ca1e21777ac76f26d0779c53f7d08e47b9e32d23bd8fed9cd', '4379626572696130363936')`<br>
Example response:
```json
[
  {
    "policy_id": "07697e6ca1e21777ac76f26d0779c53f7d08e47b9e32d23bd8fed9cd",
    "asset_name": "4379626572696130363936",
    "asset_name_ascii": "Cyberia0696",
    "fingerprint": "asset1hf3u704jz0ranfa2ygnq4028ht4vgqz8gsgw70",
    "minting_tx_hash": "f17b6fafbd1760d5d9defc0334c6a74926fd61a126842ac640b40ffb9c551a31",
    "total_supply": "1",
    "mint_cnt": 1,
    "burn_cnt": 0,
    "creation_time": 1665182000,
    "minting_tx_metadata": {
      "721": {
        "nonce": "4f0b0a78bc757e05",
        "07697e6ca1e21777ac76f26d0779c53f7d08e47b9e32d23bd8fed9cd": {
          "Cyberia0696": {
            "Pose": "Warrior II Pose - Virabhadrasana II",
            "Skin": "Red",
            "name": "Cyberia Chakra Planet #0696",
            "files": [
              {
                "src": "ipfs://QmZR6VJJ1hWx2bqKo1o8AUzoMxwrUiqGZMzZv8uHXt7MJX",
                "name": "Please wait while your experience below loads.",
                "mediaType": "image/jpg"
              },
              {
                "src": "ipfs://QmXQSmnRVL4TH4h5YYxZr2m6rfDe65hyv1J4An9znKJr9d",
                "mediaType": "text/html"
              }
            ],
            "image": "ipfs://QmZR6VJJ1hWx2bqKo1o8AUzoMxwrUiqGZMzZv8uHXt7MJX",
            "Artist": "Srink",
            "Avatar": "Male",
            "Chakra": "Root - Muladhara",
            "Mantra": "LAM",
            "Discord": "https://dsc.gg/cyberiacnft",
            "Twitter": "https://twitter.com/cyberiaCNFT",
            "Website": "https://cyberia.gg/",
            "Function": "Grounding",
            "Location": "Base of Spine",
            "Collection": "Chakra Planets",
            "Planet colour": "Red"
          }
        }
      }
    },
    "token_registry_metadata": null
  }
]
```

#### get_asset_info_bulk
Get the information of a list of assets including first minting & token registry metadata<br>
Parameters:<br>
Assets List in tge following format: `['policy.name_hex']`<br>
Returns: List of assets including first minting & token registry metadata<br>
Example:<br>
`asset_info_bulk = get_asset_info_bulk(['221b1b9ebccab1512262347491557279ac0afac63b4fbd10fc596c8a.437562656e7369734d757368726f6f6d', '221b1b9ebccab1512262347491557279ac0afac63b4fbd10fc596c8a.417a7a69654d757368726f6f6d'])`<br>
Example response:
```json
[
  {
    "policy_id": "221b1b9ebccab1512262347491557279ac0afac63b4fbd10fc596c8a",
    "asset_name": "437562656e7369734d757368726f6f6d",
    "asset_name_ascii": "CubensisMushroom",
    "fingerprint": "asset1csgmd2qwycgmqdck4dgqzzwm7xclhkqrhxs2pw",
    "minting_tx_hash": "c29fd9f0c71793eb06e7cf055e8529740b0486a802b8e9019df4853c6dec03a0",
    "total_supply": "7576",
    "mint_cnt": 1,
    "burn_cnt": 0,
    "creation_time": 1680393600,
    "minting_tx_metadata": {
      "721": {
        "version": "1.0",
        "221b1b9ebccab1512262347491557279ac0afac63b4fbd10fc596c8a": {
          "CubensisMushroom": {
            "name": "CubensisMushroom",
            "files": [
              {
                "src": "ipfs://QmQNTa19H5WnYtRiHqzNK2drC9rRTzmkxtu7tS57WZkNuZ",
                "name": "Cubensis",
                "mediaType": "image/png"
              }
            ],
            "image": "ipfs://QmQNTa19H5WnYtRiHqzNK2drC9rRTzmkxtu7tS57WZkNuZ",
            "project": "Chilled Kongs",
            "mediaType": "image/png"
          }
        }
      }
    },
    "token_registry_metadata": null
  },
  {
    "policy_id": "221b1b9ebccab1512262347491557279ac0afac63b4fbd10fc596c8a",
    "asset_name": "417a7a69654d757368726f6f6d",
    "asset_name_ascii": "AzzieMushroom",
    "fingerprint": "asset1kfskmlcvlsvpvr093staxj2788qlrkcrssf26a",
    "minting_tx_hash": "e4b94e3a5e95953acfb50e3c2fd005b2839ca79c4294b62bbf7d2afdf96dd009",
    "total_supply": "1305",
    "mint_cnt": 1,
    "burn_cnt": 0,
    "creation_time": 1680393600,
    "minting_tx_metadata": {
      "721": {
        "version": "1.0",
        "221b1b9ebccab1512262347491557279ac0afac63b4fbd10fc596c8a": {
          "AzzieMushroom": {
            "name": "AzzieMushroom",
            "files": [
              {
                "src": "ipfs://QmeAdLCKgXhxtDAcpPq5vgpRCqYWCGFMzb9jx4YEif3nWR",
                "name": "Azzie",
                "mediaType": "image/png"
              }
            ],
            "image": "ipfs://QmeAdLCKgXhxtDAcpPq5vgpRCqYWCGFMzb9jx4YEif3nWR",
            "project": "Chilled Kongs",
            "mediaType": "image/png"
          }
        }
      }
    },
    "token_registry_metadata": null
  }
]
```

#### get_asset_history
Get the mint/burn history of an asset<br>
Parameters:<br>
Asset Policy<br>
Asset Name in hexadecimal format (optional), default: all policy assets<br>
Returns: List of dictionaries with the mint/burn history of an asset<br>
Example:<br>
`asset_history = get_asset_history('07697e6ca1e21777ac76f26d0779c53f7d08e47b9e32d23bd8fed9cd', '4379626572696130363936')`<br>
Example response:
```json
[
  {
    "policy_id": "07697e6ca1e21777ac76f26d0779c53f7d08e47b9e32d23bd8fed9cd",
    "asset_name": "4379626572696130363936",
    "fingerprint": "asset1hf3u704jz0ranfa2ygnq4028ht4vgqz8gsgw70",
    "minting_txs": [
      {
        "tx_hash": "f17b6fafbd1760d5d9defc0334c6a74926fd61a126842ac640b40ffb9c551a31",
        "block_time": 1665182000,
        "quantity": "1",
        "metadata": [
          {
            "key": "721",
            "json": {
              "nonce": "4f0b0a78bc757e05",
              "07697e6ca1e21777ac76f26d0779c53f7d08e47b9e32d23bd8fed9cd": {
                "Cyberia0696": {
                  "Pose": "Warrior II Pose - Virabhadrasana II",
                  "Skin": "Red",
                  "name": "Cyberia Chakra Planet #0696",
                  "files": [
                    {
                      "src": "ipfs://QmZR6VJJ1hWx2bqKo1o8AUzoMxwrUiqGZMzZv8uHXt7MJX",
                      "name": "Please wait while your experience below loads.",
                      "mediaType": "image/jpg"
                    },
                    {
                      "src": "ipfs://QmXQSmnRVL4TH4h5YYxZr2m6rfDe65hyv1J4An9znKJr9d",
                      "mediaType": "text/html"
                    }
                  ],
                  "image": "ipfs://QmZR6VJJ1hWx2bqKo1o8AUzoMxwrUiqGZMzZv8uHXt7MJX",
                  "Artist": "Srink",
                  "Avatar": "Male",
                  "Chakra": "Root - Muladhara",
                  "Mantra": "LAM",
                  "Discord": "https://dsc.gg/cyberiacnft",
                  "Twitter": "https://twitter.com/cyberiaCNFT",
                  "Website": "https://cyberia.gg/",
                  "Function": "Grounding",
                  "Location": "Base of Spine",
                  "Collection": "Chakra Planets",
                  "Planet colour": "Red"
                }
              }
            }
          }
        ]
      }
    ]
  }
]
```

#### get_policy_asset_addresses
Get the list of addresses with quantity for each asset on the given policy<br>
Parameters: Asset Policy<br>
Returns: List of addresses with quantity for each asset on the given policy<br>
Example:<br>
`asset_policy_info = get_policy_asset_addresses('07697e6ca1e21777ac76f26d0779c53f7d08e47b9e32d23bd8fed9cd')`<br>
Example response:
```json
[
  {
    "asset_name": "4379626572696130303233",
    "payment_address": "addr1qxu5vk5xafdp39d95ya06d6uya8ldua7crpdzd2an07uw8mrtndmfr0d4qarvgj2wasdwlvrnlqt262jn5asnws7aekssq73gf",
    "quantity": "1"
  },
  {
    "asset_name": "4379626572696130303330",
    "payment_address": "addr1q9wj7ylly5nz2kel6huy966tcsw2l3ct9at7m3euhfxyv246nlp3dj9pda2rphtzycwexsaapyk73k25y3j5neyhg45s879sk4",
    "quantity": "1"
  },
  ...
  {
    "asset_name": "4379626572696132383338",
    "payment_address": "addr1qxg2l50ryn6z23543v6nujvkql9zwj7f7hvsjwalw6jvf25n5k332a42ge9w5en95g9af59fft32g0la0qtfr9vfyyesccney2",
    "quantity": "1"
  }
]
```


#### get_policy_asset_info
Get the list of asset under the given policy (including balances)<br>
Parameters: Asset Policy<br>
Returns: List of dictionaries with the policy assets<br>
Example:<br>
`asset_policy_info = get_policy_asset_info('07697e6ca1e21777ac76f26d0779c53f7d08e47b9e32d23bd8fed9cd')`<br>
Example response:
```json
[
  {
    "asset_name": "",
    "asset_name_ascii": "",
    "fingerprint": "asset1pht97cylpt7azuu9mwhmd9c9zdgmumwrrm5yrc",
    "minting_tx_metadata": {
      "key": "777",
      "json": {
        "addr": [
          "addr1qy36jns6h4w4f80u6xed49k6qn9c7tk4x4us5kaxztjq8x3un2me8nvc5ke",
          "gvll0gnwlj2ypzfhhqpns47u76gafttmq208x4d"
        ],
        "rate": "0.05"
      }
    },
    "token_registry_metadata": null,
    "total_supply": "0",
    "creation_time": 1665161713
  },
  {
    "asset_name": "4379626572696130353930",
    "asset_name_ascii": "Cyberia0590",
    "fingerprint": "asset1dzurenp8f6n8zu3lwglrs0g54xnmd5xwqe9yqp",
    "minting_tx_metadata": {
      "key": "721",
      "json": {
        "nonce": "ac2834e7b5707c30",
        "07697e6ca1e21777ac76f26d0779c53f7d08e47b9e32d23bd8fed9cd": {
          "Cyberia0590": {
            "Pose": "Warrior II Pose - Virabhadrasana II",
            "Skin": "Red",
            "name": "Cyberia Chakra Planet #0590",
            "files": [
              {
                "src": "ipfs://QmZR6VJJ1hWx2bqKo1o8AUzoMxwrUiqGZMzZv8uHXt7MJX",
                "name": "Please wait while your experience below loads.",
                "mediaType": "image/jpg"
              },
              {
                "src": "ipfs://QmXQSmnRVL4TH4h5YYxZr2m6rfDe65hyv1J4An9znKJr9d",
                "mediaType": "text/html"
              }
            ],
            "image": "ipfs://QmZR6VJJ1hWx2bqKo1o8AUzoMxwrUiqGZMzZv8uHXt7MJX",
            "Artist": "Srink",
            "Avatar": "Male",
            "Chakra": "Root - Muladhara",
            "Mantra": "LAM",
            "Discord": "https://dsc.gg/cyberiacnft",
            "Twitter": "https://twitter.com/cyberiaCNFT",
            "Website": "https://cyberia.gg/",
            "Function": "Grounding",
            "Location": "Base of Spine",
            "Collection": "Chakra Planets",
            "Planet colour": "Red"
          }
        }
      }
    },
    "token_registry_metadata": null,
    "total_supply": "1",
    "creation_time": 1665180305
  },
  ...
  {
    "asset_name": "4379626572696131313535",
    "asset_name_ascii": "Cyberia1155",
    "fingerprint": "asset1c7ymj2plmz9dddyx80axrpwy8uhm8q4hzdg3g7",
    "minting_tx_metadata": {
      "key": "721",
      "json": {
        "nonce": "18501ab3c76e955b",
        "07697e6ca1e21777ac76f26d0779c53f7d08e47b9e32d23bd8fed9cd": {
          "Cyberia0921": {
            "Pose": "Headstand - Sirsasana",
            "Skin": "Gold",
            "name": "Cyberia Chakra Planet #0921",
            "files": [
              {
                "src": "ipfs://QmaNEfYXpqFM3vRdvhUkccFpSHUc6MpA6D1Jriefz5oaZr",
                "name": "Please wait while your experience below loads.",
                "mediaType": "image/jpg"
              },
              {
                "src": "ipfs://QmT22qfNW8Ts3FcfbLTe1jx2L7XfJaxzuqKLZ9Qiw45srk",
                "mediaType": "text/html"
              }
            ],
            "image": "ipfs://QmaNEfYXpqFM3vRdvhUkccFpSHUc6MpA6D1Jriefz5oaZr",
            "Artist": "Srink",
            "Avatar": "Male",
            "Chakra": "Crown - Sahasrara",
            "Mantra": "OM",
            "Discord": "https://dsc.gg/cyberiacnft",
            "Twitter": "https://twitter.com/cyberiaCNFT",
            "Website": "https://cyberia.gg/",
            "Function": "Spiritual Connection",
            "Location": "Top of the Head",
            "Collection": "Chakra Planets",
            "Planet colour": "Purple"
          },
          "Cyberia1155": {
            "Pose": "Headstand - Sirsasana",
            "Skin": "Purple",
            "name": "Cyberia Chakra Planet #1155",
            "files": [
              {
                "src": "ipfs://QmdRbAZpWvrXQ1wDqWL7fhifJfd6dowx4oZpufdWFiG5Qo",
                "name": "Please wait while your experience below loads.",
                "mediaType": "image/jpg"
              },
              {
                "src": "ipfs://QmfC6r68AzrQyN17Yns4fhtVY4HE9FCPdtv5bsBgfac1qD",
                "mediaType": "text/html"
              }
            ],
            "image": "ipfs://QmdRbAZpWvrXQ1wDqWL7fhifJfd6dowx4oZpufdWFiG5Qo",
            "Artist": "Srink",
            "Avatar": "Female",
            "Chakra": "Crown - Sahasrara",
            "Mantra": "OM",
            "Discord": "https://dsc.gg/cyberiacnft",
            "Twitter": "https://twitter.com/cyberiaCNFT",
            "Website": "https://cyberia.gg/",
            "Function": "Spiritual Connection",
            "Location": "Top of the Head",
            "Collection": "Chakra Planets",
            "Planet colour": "Purple"
          }
        }
      }
    },
    "token_registry_metadata": null,
    "total_supply": "1",
    "creation_time": 1670493734
  }
]
```

#### get_policy_asset_list
Get the list of asset under the given policy (including balances)<br>
Parameters: Asset Policy<br>
Returns: List of dictionaries with the asset under the given policy<br>
Example:<br>
`asset_policy_list = get_policy_asset_list('07697e6ca1e21777ac76f26d0779c53f7d08e47b9e32d23bd8fed9cd')`<br>
Example response:
```json
[
  {
    "asset_name": "",
    "asset_name_ascii": "",
    "fingerprint": "asset1pht97cylpt7azuu9mwhmd9c9zdgmumwrrm5yrc",
    "minting_tx_hash": "90415fda215ff5098d7fa1385c7358c589066332068b720380726e3ef0b26de4",
    "total_supply": "0",
    "mint_cnt": 1,
    "burn_cnt": 1,
    "creation_time": 1665100800,
    "minting_tx_metadata": {
      "777": {
        "addr": [
          "addr1qy36jns6h4w4f80u6xed49k6qn9c7tk4x4us5kaxztjq8x3un2me8nvc5ke",
          "gvll0gnwlj2ypzfhhqpns47u76gafttmq208x4d"
        ],
        "rate": "0.05"
      }
    },
    "token_registry_metadata": null
  },
  ...
  {
    "asset_name": "4379626572696130333939",
    "asset_name_ascii": "Cyberia0399",
    "fingerprint": "asset1g7tgq2ly8uhtzcz79uhay8tq46h9rq62arfm8s",
    "minting_tx_hash": "98db0a36106a92149b256887f6300f2b228e14d24d488e4b1614920083cd64ff",
    "total_supply": "1",
    "mint_cnt": 1,
    "burn_cnt": 0,
    "creation_time": 1665187200,
    "minting_tx_metadata": {
      "721": {
        "nonce": "c966f455d3e03537",
        "07697e6ca1e21777ac76f26d0779c53f7d08e47b9e32d23bd8fed9cd": {
          "Cyberia0399": {
            "Pose": "Lunge pose - Anjaneyasana",
            "Skin": "Gold",
            "name": "Cyberia Chakra Planet #0399",
            "files": [
              {
                "src": "ipfs://QmVsMggcQE3da9xuZv7uvJRH84gs5ebGQ8kxVPSQw52XRf",
                "name": "Please wait while your experience below loads.",
                "mediaType": "image/jpg"
              },
              {
                "src": "ipfs://QmSHyNm11PrqyrUXszKtsz52ADH6A934c3gw41H7CMCj7D",
                "mediaType": "text/html"
              }
            ],
            "image": "ipfs://QmVsMggcQE3da9xuZv7uvJRH84gs5ebGQ8kxVPSQw52XRf",
            "Artist": "Srink",
            "Avatar": "Male",
            "Chakra": "Sacral - Svadhisthana",
            "Mantra": "VAM",
            "Discord": "https://dsc.gg/cyberiacnft",
            "Twitter": "https://twitter.com/cyberiaCNFT",
            "Website": "https://cyberia.gg/",
            "Function": "Sexual and Creative Energy",
            "Location": "Below the Belly Button",
            "Collection": "Chakra Planets",
            "Planet colour": "Orange"
          },
          "Cyberia2795": {
            "Pose": "Headstand - Sirsasana",
            "Skin": "Gold",
            "name": "Cyberia Chakra Planet #2795",
            "files": [
              {
                "src": "ipfs://QmZ4TGY2Jzy5JGaD3S7RLsrP9K8jbp44e7463iHAGitM5a",
                "name": "Please wait while your experience below loads.",
                "mediaType": "image/jpg"
              },
              {
                "src": "ipfs://QmcEqKkAcxeGNZimSiQZ2duZA4sx4xJawh35VwuJoS3A9m",
                "mediaType": "text/html"
              }
            ],
            "image": "ipfs://QmZ4TGY2Jzy5JGaD3S7RLsrP9K8jbp44e7463iHAGitM5a",
            "Artist": "Srink",
            "Avatar": "Female",
            "Chakra": "Crown - Sahasrara",
            "Mantra": "OM",
            "Discord": "https://dsc.gg/cyberiacnft",
            "Twitter": "https://twitter.com/cyberiaCNFT",
            "Website": "https://cyberia.gg/",
            "Function": "Spiritual Connection",
            "Location": "Top of the Head",
            "Collection": "Chakra Planets",
            "Planet colour": "Purple"
          }
        }
      }
    },
    "token_registry_metadata": null
  }
]
```

#### get_asset_summary
Get the summary of an asset (total transactions exclude minting/total wallets include only wallets with asset balance)<br>
Parameters:<br>
Asset Policy<br>
Asset Name in hexadecimal format (optional), default: all policy assets<br>
Returns: List of dictionaries with the mint/burn history of an asset<br>
Example:<br>
`asset_summary = get_asset_summary('07697e6ca1e21777ac76f26d0779c53f7d08e47b9e32d23bd8fed9cd', '4379626572696131313535')`<br>
Example response:
```json
[
  {
    "policy_id": "07697e6ca1e21777ac76f26d0779c53f7d08e47b9e32d23bd8fed9cd",
    "asset_name": "4379626572696131313535",
    "fingerprint": "asset1c7ymj2plmz9dddyx80axrpwy8uhm8q4hzdg3g7",
    "total_transactions": 1,
    "staked_wallets": 0,
    "unstaked_addresses": 0
  }
]
```

#### get_asset_txs
Get the list of all asset transaction hashes (the newest first)<br>
Parameters:<br>
Asset Policy<br>
Asset Name in hexadecimal format (optional), default: all policy assets<br>
Block number (optional) - return only the transactions after this block<br>
History boolean (optional) - include all historical transactions, setting to false includes only the non-empty ones<br>
Returns: List of dictionaries with the mint/burn history of an asset<br>
Example:<br>
`asset_txs = get_asset_txs('07697e6ca1e21777ac76f26d0779c53f7d08e47b9e32d23bd8fed9cd', '4379626572696131313535')`<br>
Example response:
```json
[
  {
    "tx_hash": "d4ac560398b95e6435bd6657e39fe5638f7c5bfaa6ffa6b8fa9bfae0b4882666",
    "epoch_no": 380,
    "block_height": 8112717,,
    "block_time": 1670493734
  }
]
```

### Pool

#### get_pools_list
A list of all currently registered/retiring (not retired) pools<br>
Parameters: none<br>
Returns: The list of stake pool dictionaries<br>
Example:<br>
`pool_list = get_pool_list()`<br>
Example response:
```json
[
  {
    "pool_id_bech32": "pool100wj94uzf54vup2hdzk0afng4dhjaqggt7j434mtgm8v2gfvfgp",
    "ticker": "JFLD"
  },
  {
    "pool_id_bech32": "pool102s2nqtea2hf5q0s4amj0evysmfnhrn4apyyhd4azcmsclzm96m",
    "ticker": "YULI"
  },
  ...
  {
    "pool_id_bech32": "pool12wpfng6cu7dz38yduaul3ngfm44xhv5xmech68m5fwe4wu77udd",
    "ticker": "APEX"
  },
  ...
]
```

#### get_pool_info
Current pool statuses and details for a specified list of pool ids<br>
Parameters: Stake pool bech32 ID as string (for one stake pool) or list of stake pool bech32 IDs (for multiple stake pools)<br>
Returns: Current pool(s) status(es) and details<br>
Example:<br>
`pool_info = get_pool_info('pool10ljdn3zwsh7vjkxf6t250423l5qy487x83st7m8a53jxznrkw5g')`<br>
Example response:
```json
[
  {
    "pool_id_bech32": "pool10ljdn3zwsh7vjkxf6t250423l5qy487x83st7m8a53jxznrkw5g",
    "pool_id_hex": "7fe4d9c44e85fcc958c9d2d547d551fd004a9fc63c60bf6cfda46461",
    "active_epoch_no": 214,
    "vrf_key_hash": "d163c63c5d8d668942542926945f19b89264d4d3ed469dc7fa2741c52f102aec",
    "margin": 0.005,
    "fixed_cost": "340000000",
    "pledge": "1200000000000",
    "reward_addr": "stake1u9ea9tc86xqvg6jqafhk8gz2j36csqe6gqtsd0yq7usr0eg4y2625",
    "owners": [
      "stake1u9sfwmw28cmv5c7fg60jygjk3035ssh893ece9y7qph5cpcy9xwk2",
      "stake1uxlxz7gsrmxnfa23eg7n08t9dw3lk9kmhvpunc32ascazls0xyq8s"
    ],
    "relays": [
      {
        "dns": "rl1.fortunepool.net",
        "srv": null,
        "ipv4": null,
        "ipv6": null,
        "port": 6000
      },
      {
        "dns": "rl2.fortunepool.net",
        "srv": null,
        "ipv4": null,
        "ipv6": null,
        "port": 6000
      },
      ...
      {
        "dns": "rl12.fortunepool.net",
        "srv": null,
        "ipv4": null,
        "ipv6": null,
        "port": 6000
      }
    ],
    "meta_url": "http://poolpros.tech/poolMetaData.json",
    "meta_hash": "1b085d187182cc78f3e9755c8b40b21050e710fe4a1067f9a2dbda8cadf342ba",
    "meta_json": {
      "name": "FORTUNE Pool",
      "ticker": "FORT",
      "homepage": "http://fortunepool.net",
      "description": "FORTUNE Pool -  A secure Cardano (ADA) stakepool with reliable uptime, high pledge and great rewards for delegators. Delegate with us and make your ADA FORTUNE"
    },
    "pool_status": "registered",
    "retiring_epoch": null,
    "op_cert": "1c6b83ff17b31a05046cf660c2a02c852e50eacfa60d89b89ab16aafa7797fc2",
    "op_cert_counter": 9,
    "active_stake": "4942731898587",
    "sigma": 0.00019699539760911983,
    "block_count": 722,
    "live_pledge": "1255022000000",
    "live_stake": "4939842959490",
    "live_delegators": 89,
    "live_saturation": 7.01
  }
]
```

#### get_pool_stake_snapshot
Returns Mark, Set and Go stake snapshots for the selected pool, useful for leaderlog calculation<br>
Parameters: Stake pool bech32 id<br>
Returns: Pool snapshot as list of dictionaries by epoch (current and previous 2)<br>
Example:<br>
`pool_stake_snapshot = get_pool_stake_snapshot('pool155efqn9xpcf73pphkk88cmlkdwx4ulkg606tne970qswczg3asc')`<br>
Example response:
```json
[
  {
    "snapshot": "Go",
    "epoch_no": 380,
    "nonce": "3950677ef48bb212ad335f253ad1998be4e9fe4ae2a26d402607850461398125",
    "pool_stake": "64328594406327",
    "active_stake": "25065309972207037"
  },
  {
    "snapshot": "Set",
    "epoch_no": 381,
    "nonce": "4d617a9da289e6ff2574cc737ac22b337c6d2766847d3422db519f137dee7c43",
    "pool_stake": "64328594406327",
    "active_stake": "25090595813788584"
  },
  {
    "snapshot": "Mark",
    "epoch_no": 382,
    "nonce": null,
    "pool_stake": "64328594406327",
    "active_stake": "25079111896910089"
  }
]
```

#### get_pool_delegators
Returns information about live delegators for a given pool<br>
Parameters Stake pool bech32 id<br>
Returns: The list of pool delegators dictionaries<br>
Example:<br>
`pool_delegators = get_pool_delegators('pool12wpfng6cu7dz38yduaul3ngfm44xhv5xmech68m5fwe4wu77udd')`<br>
Example response:
```json
[
  {
    "stake_address": "stake1u80603g5n7vtycl75c60jmv56jx3cw53v23xv0txkpcu8kcwr2k27",
    "amount": "852345",
    "active_epoch_no": 328,
    "latest_delegation_tx_hash": "2c91c8497df98e6a51bf8c05222af8e7b195847764e4a4407afe2504e0773fc7"
  },
  {
    "stake_address": "stake1u82mfrr9ztql37er3hy73rtpccuv5fmet2lrrudmzdrm6qgpf22jy",
    "amount": "244092618",
    "active_epoch_no": 323,
    "latest_delegation_tx_hash": "3594999b3aff5f33490a8ad4611f844efd305782403a8e51067f3ea4721ce821"
  },
  ...
  {
    "stake_address": "stake1uyzwh2mwjwphgs7kxvd7s8jn640plxf368wj0syftewl0nq06vlqu",
    "amount": "103417951621",
    "active_epoch_no": 323,
    "latest_delegation_tx_hash": "7193e5702d1cac1255c9dac8efe8368abda5b7b6c58b515467b8e2e1ca07d2be"
  }
]
```

#### get_pool_delegators_history
Returns information about active delegators (incl. history) for a given pool and epoch number (all epochs if not specified)<br>
Parameters:<br>
Stake pool bech32 id<br>
Epoch (optional)<br>
Returns: The list of pool delegators dictionaries<br>
Example:<br>
`pool_delegators_history = get_pool_delegators_history('pool12wpfng6cu7dz38yduaul3ngfm44xhv5xmech68m5fwe4wu77udd', 380)`<br>
Example response:
```json
[
  {
    "stake_address": "stake1uyezz2wzt4rl5wug8ju8zshvfzkw2lksw8jfp0wpueq2nccnnkwxh",
    "amount": "1043563298281",
    "epoch_no": 380
  },
  {
    "stake_address": "stake1uxptzz4gkehxj5ht85xdjmad5qt0mc00dxmyxd84e2dgrvsla9k0u",
    "amount": "1010182386722",
    "epoch_no": 380
  },
  ...
  {
    "stake_address": "stake1uxkm4akqqkkt2ayqwnj5wgex4hddgq65st892cz33ez726q9lf3un",
    "amount": "45053",
    "epoch_no": 380
  }
]
```

#### get_pool_blocks
Returns information about blocks minted by a given pool for all epochs (or _epoch_no if provided)<br>
Parameters:<br>
Stake pool bech32 id<br>
Epoch (optional)<br>
Returns: The list of pool blocks dictionaries<br>
Example:<br>
`pool_blocks = get_pool_blocks('pool12wpfng6cu7dz38yduaul3ngfm44xhv5xmech68m5fwe4wu77udd', 380)`<br>
Example response:
```json
[
  {
    "epoch_no": 380,
    "epoch_slot": 98385,
    "abs_slot": 78895185,
    "block_height": 8111118,
    "block_hash": "043b2d7b5d125d9f891aa12ad04976be4c3f1ce862b71aff3352dd76be943ae5",
    "block_time": 1670461476
  },
  {
    "epoch_no": 380,
    "epoch_slot": 381300,
    "abs_slot": 79178100,
    "block_height": 8125194,
    "block_hash": "c6c811e01decdf241465e5b63684917f48fa11556ff04b22ae46d112703a19dc",
    "block_time": 1670744391
  }
]
```

#### get_pool_history
Returns information about pool stake, block and reward history in a given epoch (or all epochs that pool existed for, in descending order if no epoch number was provided)<br>
Parameters:<br>
Stake pool bech32 id<br>
Epoch (optional)<br>
Returns:  Information about pool stake, block and reward history as a list dictionaries by epoch (descending)<br>
Example:<br>
`pool_history = get_pool_history('pool12wpfng6cu7dz38yduaul3ngfm44xhv5xmech68m5fwe4wu77udd', 379)`<br>
Example response:
```json
[
  {
    "epoch_no": 379,
    "active_stake": "3158165931346",
    "active_stake_pct": 0.012602983456573744,
    "saturation_pct": 4.48,
    "block_cnt": 4,
    "delegator_cnt": 200,
    "margin": 0.0199,
    "fixed_cost": "340000000",
    "pool_fees": "380697027",
    "deleg_rewards": "2004379694",
    "epoch_ros": 4.74052366
  }
]
```

#### get_pool_updates
Returns all pool updates for all pools or only updates for specific pool if specified<br>
Parameters: Stake pool bech32 id (optional)<br>
Returns: pool updates as a list of dictionaries<br>
Example:<br>
`pool_updates = get_pool_updates('pool12wpfng6cu7dz38yduaul3ngfm44xhv5xmech68m5fwe4wu77udd')`<br>
Example response:
```json
[
  {
    "tx_hash": "6358622ef9c7a395aaf1590661330a17095fef3c39caa2ae319c737c85bfacb9",
    "block_time": 1665138387,
    "pool_id_bech32": "pool12wpfng6cu7dz38yduaul3ngfm44xhv5xmech68m5fwe4wu77udd",
    "pool_id_hex": "538299a358e79a289c8de779f8cd09dd6a6bb286de717d1f744bb357",
    "active_epoch_no": 370,
    "vrf_key_hash": "d32b8a284fb259478909aebb4d465d0e2c214ab187d905006da624de023cff7a",
    "margin": 0.0199,
    "fixed_cost": "340000000",
    "pledge": "25000000000",
    "reward_addr": "stake1u8mpqafgs22r32cfmkwey9ypjuyl0q0wj2qycxadcjrk0kqu7qh8n",
    "owners": [
      "stake1uxpdrerp9wrxunfh6ukyv5267j70fzxgw0fr3z8zeac5vyqhf9jhy",
      "stake1uxey9c4w4dlrym6yayltuwmgzucm6068y3spmvan43t2zhs4l9r7f",
      "stake1u87djlkkkfehdmxq5zu4nwg7np065kyrr3j38wagcsr56pqc3u0zj"
    ],
    "relays": [
      {
        "dns": "relay1.apexpool.info",
        "srv": null,
        "ipv4": null,
        "ipv6": null,
        "port": 6000
      },
      {
        "dns": "relay2.apexpool.info",
        "srv": null,
        "ipv4": null,
        "ipv6": null,
        "port": 6000
      }
    ],
    "meta_url": "https://apexpool.info/poolmetadata.json",
    "meta_hash": "82e5f297f2145badd7b03f02a215fc4478772d0df3818e21e36738be48ccc55c",
    "meta_json": null,
    "pool_status": "registered",
    "retiring_epoch": null
  },
  {
    "tx_hash": "0b8fc5e712d6232c2ce2fe64243e6a9ecdc5419a490e929914c2d31d4153e66a",
    "block_time": 1649591452,
    "pool_id_bech32": "pool12wpfng6cu7dz38yduaul3ngfm44xhv5xmech68m5fwe4wu77udd",
    "pool_id_hex": "538299a358e79a289c8de779f8cd09dd6a6bb286de717d1f744bb357",
    "active_epoch_no": 334,
    "vrf_key_hash": "d32b8a284fb259478909aebb4d465d0e2c214ab187d905006da624de023cff7a",
    "margin": 0.0199,
    "fixed_cost": "340000000",
    "pledge": "25000000000",
    "reward_addr": "stake1uxpdrerp9wrxunfh6ukyv5267j70fzxgw0fr3z8zeac5vyqhf9jhy",
    "owners": [
      "stake1uxpdrerp9wrxunfh6ukyv5267j70fzxgw0fr3z8zeac5vyqhf9jhy",
      "stake1uxey9c4w4dlrym6yayltuwmgzucm6068y3spmvan43t2zhs4l9r7f",
      "stake1u87djlkkkfehdmxq5zu4nwg7np065kyrr3j38wagcsr56pqc3u0zj"
    ],
    "relays": [
      {
        "dns": "relay1.apexpool.info",
        "srv": null,
        "ipv4": null,
        "ipv6": null,
        "port": 6000
      },
      {
        "dns": "relay2.apexpool.info",
        "srv": null,
        "ipv4": null,
        "ipv6": null,
        "port": 6000
      }
    ],
    "meta_url": "https://apexpool.info/poolmetadata.json",
    "meta_hash": "82e5f297f2145badd7b03f02a215fc4478772d0df3818e21e36738be48ccc55c",
    "meta_json": null,
    "pool_status": "registered",
    "retiring_epoch": null
  },
  ...
]
```

#### get_pool_relays
A list of registered relays for all currently registered/retiring (not retired) pools<br>
Parameters: none<br>
Returns: The list of relays dictionaries by stake pool<br>
Example:<br>
`pool_relays = get_pool_relays()`<br>
Example response:
```json
[
  {
    "pool_id_bech32": "pool100wj94uzf54vup2hdzk0afng4dhjaqggt7j434mtgm8v2gfvfgp",
    "relays": [
      {
        "dns": null,
        "srv": null,
        "ipv4": "165.232.146.185",
        "ipv6": null,
        "port": 3000
      }
    ]
  },
  {
    "pool_id_bech32": "pool102s2nqtea2hf5q0s4amj0evysmfnhrn4apyyhd4azcmsclzm96m",
    "relays": []
  },
  ...
  {
    "pool_id_bech32": "pool1auvwj75q70s7jce63nvptujs6460kvyxqn0wjegkz4mhja7g5t6",
    "relays": [
      {
        "dns": null,
        "srv": null,
        "ipv4": "45.13.59.72",
        "ipv6": null,
        "port": 6000
      },
      {
        "dns": null,
        "srv": null,
        "ipv4": "45.13.59.73",
        "ipv6": null,
        "port": 6000
      }
    ]
  },
  ...
]
```

#### get_pool_metadata
A list of registered relays for all currently registered/retiring (not retired) pools<br>
Parameters: Stake pool bech32 ID(s) as string (for one stake pool) or list of stake pool bech32 IDs (for multiple stake pools)<br>
Returns: The list of pool metadata dictionaries<br>
Example:<br>
`pool_metadata = get_pool_metadata('pool1auvwj75q70s7jce63nvptujs6460kvyxqn0wjegkz4mhja7g5t6')`<br>
Example response:
```json
[
  {
    "pool_id_bech32": "pool1auvwj75q70s7jce63nvptujs6460kvyxqn0wjegkz4mhja7g5t6",
    "meta_url": "https://git.io/J1yfm",
    "meta_hash": "e123e7e59922deab90ff06642500c69cafe03933f0854b1534a829cbae2cf472",
    "meta_json": {
      "name": "Innovatio",
      "ticker": "INNV",
      "homepage": "https://www.innovatiofounder.com/",
      "description": "Pool focused on the expansion of the Innovatio brand and its financial services and to the support of the community of entrepreneurs and freelancers of the blockchain ecosystem"
    }
  }
]
```

#### get_retiring_pools
Get the retiring stake pools list<br>
Parameters: none<br>
Returns: The list of retiring pools dictionaries<br>
Example:<br>
`retiring_pools = get_retiring_pools()`<br>
Example response:
```json
[
  {
    "tx_hash": "39a046ef9b5b9e149d24bae8c86f6fb93b08d57312615d22b6a3e73279198e73",
    "block_time": 1667610905,
    "pool_id_bech32": "pool1a8z4kxgsul7u4nedkxlx7g86mlcwt45dv4ntygmfsqc6kdse5c7",
    "pool_id_hex": "e9c55b1910e7fdcacf2db1be6f20fadff0e5d68d6566b223698031ab",
    "active_epoch_no": 375,
    "vrf_key_hash": "8ad95d9965ca817e7d7d5d6985ba4c92b77a206250fa59f52acb6ab36507c79b",
    "margin": 0,
    "fixed_cost": "340000000",
    "pledge": "2000000",
    "reward_addr": "stake1uyyyeu9dl8l8tvly08nvsdm8dwu9q94w3ywxyn84jqz2qzgm6a42u",
    "owners": [
      "stake1uyyyeu9dl8l8tvly08nvsdm8dwu9q94w3ywxyn84jqz2qzgm6a42u"
    ],
    "relays": [
      {
        "dns": null,
        "srv": null,
        "ipv4": "158.140.192.143",
        "ipv6": null,
        "port": 3001
      }
    ],
    "meta_url": "https://raw.githubusercontent.com/etsraphael/Cardano/p/p.json",
    "meta_hash": "dee0758d3212808f99698e96446dd9400b4455d5c44286f91f66dd6c5796d064",
    "meta_json": null,
    "pool_status": "retiring",
    "retiring_epoch": 391
  },
  {
    "tx_hash": "e91b2fe2fdd88af555ff28a4e9bc0c2cd0d7d403f84bf76095ddef9696960222",
    "block_time": 1623852340,
    "pool_id_bech32": "pool14y230zspjkhezehue4p2d9q87xh3p8a0vnpugzdty7gwcruepps",
    "pool_id_hex": "a915178a0195af9166fccd42a69407f1af109faf64c3c409ab2790ec",
    "active_epoch_no": 275,
    "vrf_key_hash": "fc9af9335415593f9c4f171aded1fd80cb69a0e1e663a978572ace376f0a4f11",
    "margin": 0,
    "fixed_cost": "340000000",
    "pledge": "12000000000",
    "reward_addr": "stake1uyam20k8v2azz38r2jf499udyru7qfs4flaefc05h9546cqjmjnmr",
    "owners": [
      "stake1uyam20k8v2azz38r2jf499udyru7qfs4flaefc05h9546cqjmjnmr"
    ],
    "relays": [
      {
        "dns": "relay1.faststakepool.com",
        "srv": null,
        "ipv4": null,
        "ipv6": null,
        "port": 3000
      }
    ],
    "meta_url": "https://raw.githubusercontent.com/FASTstakepool/meta/master/data",
    "meta_hash": "64bdb12028955b248b2d61467aedba30388a95d175636b3b042e9c69aa710dd4",
    "meta_json": null,
    "pool_status": "retiring",
    "retiring_epoch": 392
  },
  ...
```

### Script

#### get_native_script_list
List of all existing native script hashes along with their creation transaction hashes<br>
Parameters: none<br>
Returns: The list of all native scripts dictionaries<br>
Example:<br>
`native_script_list = get_native_script_list()`<br>
Example response:
```json
[
  {
    "script_hash": "65c197d565e88a20885e535f93755682444d3c02fd44dd70883fe89e",
    "creation_tx_hash": "4a3f86762383f1d228542d383ae7ac89cf75cf7ff84dec8148558ea92b0b92d0",
    "type": "timelock",
    "script": {
      "type": "all",
      "scripts": [
        {
          "type": "sig",
          "keyHash": "a96da581c39549aeda81f539ac3940ac0cb53657e774ca7e68f15ed9"
        },
        {
          "type": "sig",
          "keyHash": "ccfcb3fed004562be1354c837a4a4b9f4b1c2b6705229efeedd12d4d"
        },
        {
          "type": "sig",
          "keyHash": "74fcd61aecebe36aa6b6cd4314027282fa4b41c3ce8af17d9b77d0d1"
        }
      ]
    }
  },
  {
    "script_hash": "00000002df633853f6a47465c9496721d2d5b1291b8398016c0e87ae",
    "creation_tx_hash": "e252be4c7e40d35919f741c9649ff207c3e49d53bb819e5c1cb458055fd363ed",
    "type": "timelock",
    "script": {
      "type": "all",
      "scripts": [
        {
          "slot": 24285375,
          "type": "before"
        },
        {
          "type": "sig",
          "keyHash": "e97316c52c85eab276fd40feacf78bc5eff74e225e744567140070c3"
        }
      ]
    }
  },
  ...
]
```

#### get_plutus_script_list
List of all existing native script hashes along with their creation transaction hashes<br>
Parameters: none<br>
Returns: The list of all plutus scripts dictionaries<br>
Example:<br>
`plutus_script_list = get_plutus_script_list()`<br>
Example response:
```json
[
  {
    "script_hash": "c916b3d14a51087cc967223aad3f2e4e5c01993f5429719c32c2061e",
    "creation_tx_hash": "ed96d6ee90c6e8e5828b0b4f5fbdcbefc28d8b7e689ac4605da56c9c58a7cd96"
  },
  {
    "script_hash": "c1996b36d11bf42103745844cc5ee9bf13fde475fa909809e2da7261",
    "creation_tx_hash": "fa36280a65610f0171bcfdb3812bc0f0f6312c08cfb39c3419287bc1d654a4ae"
  },
  {
    "script_hash": "2161af28e544066081a36a85857f8894910984ea50f5a7a1d7a345e2",
    "creation_tx_hash": "21aabf5a3f1b9162ea12d49c94c110a89c5702f0ebdb3390b40110b22a750326"
  },
  ...
]
```

#### get_script_redeemers
List of all redeemers for a given script hash<br>
Parameters: Script hash<br>
Returns: Redeemers list as dictionary<br>
Example:<br>
`script_redeemers = get_script_redeemers('c1996b36d11bf42103745844cc5ee9bf13fde475fa909809e2da7261')`<br>
Example response:
```json
[
  {
    "script_hash": "c1996b36d11bf42103745844cc5ee9bf13fde475fa909809e2da7261",
    "redeemers": [
      {
        "tx_hash": "fa36280a65610f0171bcfdb3812bc0f0f6312c08cfb39c3419287bc1d654a4ae",
        "tx_index": 0,
        "unit_mem": 1197950,
        "unit_steps": 491845099,
        "fee": "104584",
        "purpose": "mint",
        "datum_hash": "45b0cfc220ceec5b7c1c62c4d4193d38e4eba48e8815729ce75f9c0ab0e4c1c0",
        "datum_value": {
          "list": []
        }
      }
    ]
  }
]
```

#### get_datum_info
List of datum information for given datum hashes<br>
Parameters: Datum hash(es) as string (for one datum hash) or list (for a list of datum hashes)<br>
Returns Datum information as list of dictionaries<br>
Example:<br>
`datum_info = get_datum_info('45b0cfc220ceec5b7c1c62c4d4193d38e4eba48e8815729ce75f9c0ab0e4c1c0')`<br>
Example response:
```json
[
  {
    "hash": "45b0cfc220ceec5b7c1c62c4d4193d38e4eba48e8815729ce75f9c0ab0e4c1c0",
    "value": {
      "list": []
    },
    "bytes": "80"
  }
]
```

### Stake Account

#### get_account_list
Get a list of all accounts<br>
Parameters:<br>
The offset (optional) to start from, default 0<br>
The maximum number of accounts to return (optional), default 0 (no limit)<br>
Returns: The list of accounts dictionaries<br>
This takes a very long time to execute (about one hour), because the total number of accounts is in the millions range.<br>
Example:<br>
`account_list = get_account_list()`<br>
Example response:
```json
[
  {
    "id": "stake1uyfmzu5qqy70a8kq4c8rw09q0w0ktfcxppwujejnsh6tyrg5c774g"
  },
  {
    "id": "stake1uydhlh7f2kkw9eazct5zyzlrvj32gjnkmt2v5qf6t8rut4qwch8ey"
  },
  {
    "id": "stake1uxsgkz6fvgws5wn80vckwvghzapnhfmf0672nmmkm2tt9fcaau5sw"
  },
  ...
]
```

#### get_account_info
Get the account information for given stake addresses (accounts)<br>
Parameters: Stake address(es), as a string (for one address) or a list (for multiple addresses)<br>
Returns: The list of account information dictionaries<br>
Example:<br>
`account_info = get_account_info('stake1uy4jj73pfyejl4d2rs6nc70eykkhhu56p3y2rj2tdayfzeqnjyh0j')`<br>
Example response:
```json
[
  {
    "stake_address": "stake1uy4jj73pfyejl4d2rs6nc70eykkhhu56p3y2rj2tdayfzeqnjyh0j",
    "status": "registered",
    "delegated_pool": "pool18r2y72aue5nmv489xtnfxl36vzusq95qst6urd87yd5hgzms04c",
    "total_balance": "20418617",
    "utxo": "20418617",
    "rewards": "0",
    "withdrawals": "0",
    "rewards_available": "0",
    "reserves": "0",
    "treasury": "0"
  }
]
```

#### get_account_utxos
Get a list of assets registered via token registry on github<br>
Parameters: Stake address<br>
Returns: The list of all UTxOs at all payment addresses associated with the stake address<br>
Example:<br>
`account_utxos = get_account_utxos('stake1ux5r7myfhycj234wpqyhh3h8skgwvq0hsstpw52f66857uq95cas6')`
Example response:<br>
```json
[
  {
	"tx_hash": "215bcaa7b13c491db28d5525d9b2a13a7d8ddabd563da8113a449ab33a6a60be",
	"tx_index": 2,
	"address": "addr1q9dwzug2qzdsqvpvrn886nqdtwr02n9kxtwqsxce2gacvedg8akgnwf3y4r2uzqf00rw0pvsucql0pqkzag5n450facqeuerev",
	"value": "85813474",
	"block_height": 8214437,
	"block_time": 1672580966
  },
  {
	"tx_hash": "1eb26dce2f471fbe32aa8cb303f5e8d8078d1da4dbbb78a7bc135036bb3f2f9c",
	"tx_index": 0,
	"address": "addr1q88u9gz83nhs9p5pud9kyucx8sg0ygae2p9a4g2p2y55c4ag8akgnwf3y4r2uzqf00rw0pvsucql0pqkzag5n450facqqyd2n7",
	"value": "110094569",
	"block_height": 8406870,
	"block_time": 1676555396
  },
  {
	"tx_hash": "d530de851c2f867f2174c1073b04bdb9f2e2d16029fcfb488e8150ba66976d43",
	"tx_index": 0,
	"address": "addr1qxyp2wsafavj47dpc6uqgqx8se3969jn4crfk7y4zwd7vfag8akgnwf3y4r2uzqf00rw0pvsucql0pqkzag5n450facqlyvudm",
	"value": "1249900",
	"block_height": 8489290,
	"block_time": 1678248733
  },
  ...
  {
	"tx_hash": "d8e3ca8b36f9a785ff33f01aa5460f9248ea94acd621ea187093206b04aa6e30",
	"tx_index": 0,
	"address": "addr1q8txa88kt6rpdv3zzn8ghx7u4udf6rpj690rfdvlqn35fldg8akgnwf3y4r2uzqf00rw0pvsucql0pqkzag5n450facqplx97u",
	"value": "54000000",
	"block_height": 8759577,
	"block_time": 1683809438
  }
]
```

#### get_account_info_cached
Get the cached account information for given stake addresses (accounts)<br>
Parameters: Stake address(es), as a string (for one address) or a list (for multiple addresses)<br>
Returns: The list of account information dictionaries<br>
Example:<br>
`account_info_cached = get_account_info_cached('stake1uy4jj73pfyejl4d2rs6nc70eykkhhu56p3y2rj2tdayfzeqnjyh0j')`<br>
Example response:
```json
[
  {
    "stake_address": "stake1uy4jj73pfyejl4d2rs6nc70eykkhhu56p3y2rj2tdayfzeqnjyh0j",
    "status": "registered",
    "delegated_pool": "pool18r2y72aue5nmv489xtnfxl36vzusq95qst6urd87yd5hgzms04c",
    "total_balance": "20418617",
    "utxo": "20418617",
    "rewards": "0",
    "withdrawals": "0",
    "rewards_available": "0",
    "reserves": "0",
    "treasury": "0"
  }
]
```

#### get_account_rewards
Get the full rewards history (including MIR) for given stake addresses (accounts)<br>
Parameters:<br>
Stake address(es), as a string (for one address) or a list (for multiple addresses)<br>
Epoch (optional), default: current epoch<br>
Returns: The list of rewards dictionaries by account (stake address)<br>
Example:<br>
`account_rewards = get_account_rewards('stake1u8lhspu67x3jejzcfrh487rtu3hnm26cg0jsn0mgh2y6n9q9ve26z')`<br>
Example response:
```json
[
  {
    "stake_address": "stake1u8lhspu67x3jejzcfrh487rtu3hnm26cg0jsn0mgh2y6n9q9ve26z",
    "rewards": [
      {
        "earned_epoch": 233,
        "spendable_epoch": 235,
        "amount": "3990414",
        "type": "member",
        "pool_id": "pool1jdhjfcu34lq88rypdtslzwyf27uh0h3apcr9mjd68zhc69r29fy"
      },
      {
        "earned_epoch": 234,
        "spendable_epoch": 236,
        "amount": "2792902",
        "type": "member",
        "pool_id": "pool1jdhjfcu34lq88rypdtslzwyf27uh0h3apcr9mjd68zhc69r29fy"
      },
      ...
      {
        "earned_epoch": 379,
        "spendable_epoch": 381,
        "amount": "6496870",
        "type": "member",
        "pool_id": "pool12wpfng6cu7dz38yduaul3ngfm44xhv5xmech68m5fwe4wu77udd"
      }
    ]
  }
]
```

#### get_account_updates
Get the account updates (registration, deregistration, delegation and withdrawals) for given stake addresses (accounts)<br>
Parameters: Stake address(es), as a string (for one address) or a list (for multiple addresses)<br>
Returns: The list of account updates dictionaries by account (stake address)<br>
Example:<br>
`account_updates = get_account_updates('stake1u8lhspu67x3jejzcfrh487rtu3hnm26cg0jsn0mgh2y6n9q9ve26z')`<br>
Example response:
```json
[
  {
    "stake_address": "stake1u8lhspu67x3jejzcfrh487rtu3hnm26cg0jsn0mgh2y6n9q9ve26z",
    "updates": [
      {
        "action_type": "withdrawal",
        "tx_hash": "487bc75f00fe934dad33683271cca8540fe868eef7025962678f179a1a111ecc",
        "epoch_no": 324,
        "epoch_slot": 70687,
        "absolute_slot": 54675487,
        "block_time": 1646241778
      },
      {
        "action_type": "withdrawal",
        "tx_hash": "eb3ffa01f434e210716151fd9001af82529e371a91c20af02512942f988a2119",
        "epoch_no": 269,
        "epoch_slot": 339679,
        "absolute_slot": 31184479,
        "block_time": 1622750770
      },
      ...
      {
        "action_type": "withdrawal",
        "tx_hash": "b056dcbff9b908e1bd3ed015466f64486538058ba3553dbf885b216d88343370",
        "epoch_no": 252,
        "epoch_slot": 58375,
        "absolute_slot": 23559175,
        "block_time": 1615125466
      }
    ]
  }
]
```

#### get_account_addresses
Get all addresses associated with given staking accounts<br>
Parameters: Stake address(es), as a string (for one address) or a list (for multiple addresses)<br>
Returns: The list of addresses dictionaries by account (stake address)<br>
Example:<br>
`account_addresses = get_account_addresses('stake1u8lhspu67x3jejzcfrh487rtu3hnm26cg0jsn0mgh2y6n9q9ve26z')`<br>
Example response:
```json
[
  {
    "stake_address": "stake1u8lhspu67x3jejzcfrh487rtu3hnm26cg0jsn0mgh2y6n9q9ve26z",
    "addresses": [
      "addr1qxwjxvzv8rmyutcjp0647w4n05wv7aez9jdmqcxn8a9sshll0qre4udr9ny9sj8020uxher08k44ssl9pxlk3w5f4x2qjyz9yf"
    ]
  }
]
```

#### get_account_assets
Get the native asset balance of given accounts<br>
Parameters: Stake address(es), as a string (for one address) or a list (for multiple addresses)<br>
Returns: The list of account assets dictionaries by account (stake address)<br>
Example:<br>
`account_assets = get_account_assets('stake1u8lhspu67x3jejzcfrh487rtu3hnm26cg0jsn0mgh2y6n9q9ve26z')`<br>
Example response:
```json
[
  {
    "stake_address": "stake1u8lhspu67x3jejzcfrh487rtu3hnm26cg0jsn0mgh2y6n9q9ve26z",
    "asset_list": [
      {
        "policy_id": "0029cb7c88c7567b63d1a512c0ed626aa169688ec980730c0473b913",
        "asset_name": "6c70202302",
        "fingerprint": "asset1awuysx8hc686uz0dykmvmc7jfut2ulceucf6yc",
        "quantity": "418089787"
      },
      {
        "policy_id": "0029cb7c88c7567b63d1a512c0ed626aa169688ec980730c0473b913",
        "asset_name": "6c7020f302",
        "fingerprint": "asset1mcq0awl6awlaqg0ywukf94q0mnau263l9rght5",
        "quantity": "586811406"
      },
      ...
      {
        "policy_id": "ea2d23f1fa631b414252824c153f2d6ba833506477a929770a4dd9c2",
        "asset_name": "4d414442554c",
        "fingerprint": "asset1q0kwjy669gmsqpvxp4lr0sp26pdm0dafme3qp2",
        "quantity": "500"
      }
    ]
  }
]
```

#### get_account_history
Get the staking history of given stake addresses (accounts)<br>
Parameters: Stake address(es), as a string (for one address) or a list (for multiple addresses)<br>
Returns: The list of staking history dictionaries by account (stake address)<br>
Example:<br>
`account_history = get_account_history('stake1u8lhspu67x3jejzcfrh487rtu3hnm26cg0jsn0mgh2y6n9q9ve26z')`<br>
Example response:
```json
[
  {
    "stake_address": "stake1u8lhspu67x3jejzcfrh487rtu3hnm26cg0jsn0mgh2y6n9q9ve26z",
    "history": [
      {
        "pool_id": "pool1jdhjfcu34lq88rypdtslzwyf27uh0h3apcr9mjd68zhc69r29fy",
        "epoch_no": 233,
        "active_stake": "4655706122"
      },
      {
        "pool_id": "pool1jdhjfcu34lq88rypdtslzwyf27uh0h3apcr9mjd68zhc69r29fy",
        "epoch_no": 234,
        "active_stake": "5020706122"
      },
      ...
      {
        "pool_id": "pool12wpfng6cu7dz38yduaul3ngfm44xhv5xmech68m5fwe4wu77udd",
        "epoch_no": 381,
        "active_stake": "10247851319"
      }
    ]
  }
]
```
