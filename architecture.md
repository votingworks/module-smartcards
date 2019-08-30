# Architecture

This module reads and writes smartcards, mostly AT24C64 EEPROM cards.

## Card Structure

A card holds a short and a long value. The short value is something
like an identifier or a hash. At most 63 bytes. The long value can be
as long as 65,536 bytes, though for now we only support the AT24C64,
which has a capacity of 8K. The long value is not fetched by default,
as that takes a while.

Data Format on a card is:

* "VX." - 3 ascii byte identifier
* <version_number> - 1 byte
* <dataprops> - 1 byte
* the remainder of the card data depends on dataprops

## Version Number

The version number described here is v2, represented in <version_number> as 0x02.

## Data Props

The data properties of a card take up 1 byte as follows:

* <write_protection> - 1 bit
* <encryption> - 3 bits
* <unused> - 4 bits

## Encryption

The encryption field is 3 bits, with the following values:

* 0x0 - plaintext
* 0x1 - encrypted with a 6-digit PIN
* 0x2 - encrypted using AES256-GCM

## Plaintext Payload

A plaintext payload follows the <dataprops> field as follows:

* <short_value_length> - 1 byte
* <long_value_length> - 2 bytes
* <short_value> - up to 63 bytes
* <long_value> - up to 65,536 bytes capped by card type.

## PIN Encryption

A PIN-encrypted payload follows the <dataprops> field as follows:

* <salt> - 16 bytes

The salt is used to key-stretch the 6-digit PIN into a 256-bit key,
and the remainder of the data follows the AES-GCM format.

## AES-GCM encryption

An AES-GCM-encrypted payload follows the <dataprops> field (or the PIN-encryption fields) as follows:

* <iv> - 12 bytes
* <tag> - 16 bytes
* <encrypted_payload_length> - 2 bytes
* <encrypted_payload> - up to 65,500 bytes, capped by card type.

## Encrypted payload

The encrypted payload is the encryption of the plaintext payload
exactly as described above, byte by byte.
