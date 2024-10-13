# MongoDB Project Documentation

This project demonstrates the basic usage and commands of MongoDB for managing databases, collections, and documents.

## Table of Contents

- [MongoDB Project Documentation](#mongodb-project-documentation)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [Basic MongoDB Commands](#basic-mongodb-commands)
    - [Database Commands](#database-commands)
    - [Collection Commands](#collection-commands)
    - [Document Commands](#document-commands)
      - [Inserting Documents](#inserting-documents)
      - [Querying Documents](#querying-documents)
      - [Updating Documents](#updating-documents)
      - [Deleting Documents](#deleting-documents)
  - [Advanced MongoDB Commands](#advanced-mongodb-commands)
    - [Counting Documents](#counting-documents)
    - [Sorting and Limiting Results](#sorting-and-limiting-results)
    - [Indexing](#indexing)
  - [Backup and Restore](#backup-and-restore)
    - [Backup a database:](#backup-a-database)

## Introduction

MongoDB is a NoSQL database that stores data in flexible, JSON-like documents. This documentation covers the most commonly used MongoDB commands to help you manage your databases and collections efficiently.

## Requirements

- MongoDB installed on your system.
- Basic understanding of MongoDB and NoSQL databases.

## Installation

To install MongoDB, please follow the official MongoDB installation guide based on your operating system:

- [MongoDB Installation Documentation](https://docs.mongodb.com/manual/installation/)

## Basic MongoDB Commands

### Database Commands

- **Switch to a database (or create it if it doesn't exist)**:

  ```bash
  use database_name
  ```

- **Show all databases**:

  ```bash
  show dbs
  ```

- **Drop the current database**:
  ```bash
  db.dropDatabase()
  ```

### Collection Commands

- **Create a collection**:

  ```bash
  db.createCollection("collection_name")
  ```

- **Show all collections**:

  ```bash
  show collections
  ```

- **Drop a collection**:
  ```bash
  db.collection_name.drop()
  ```

### Document Commands

#### Inserting Documents

- **Insert a single document**:

  ```bash
  db.collection_name.insertOne({ field1: "value1", field2: "value2" })
  ```

- **Insert multiple documents**:
  ```bash
  db.collection_name.insertMany([{ field1: "value1" }, { field1: "value2" }])
  ```

#### Querying Documents

- **Find the first document that matches the condition**:

  ```bash
  db.collection_name.findOne({ field: "value" })
  ```

- **Find all documents that match the condition**:

  ```bash
  db.collection_name.find({ field: "value" })
  ```

- **Find all documents and show specific fields**:
  ```bash
  db.collection_name.find({}, { field1: 1, field2: 1 })
  ```

#### Updating Documents

- **Update the first document that matches the condition**:

  ```bash
  db.collection_name.updateOne({ field: "value" }, { $set: { field_to_update: "new_value" } })
  ```

- **Update all documents that match the condition**:
  ```bash
  db.collection_name.updateMany({ field: "value" }, { $set: { field_to_update: "new_value" } })
  ```

#### Deleting Documents

- **Delete the first document that matches the condition**:

  ```bash
  db.collection_name.deleteOne({ field: "value" })
  ```

- **Delete all documents that match the condition**:
  ```bash
  db.collection_name.deleteMany({ field: "value" })
  ```

## Advanced MongoDB Commands

### Counting Documents

- **Count all documents in a collection**:

  ```bash
  db.collection_name.countDocuments()
  ```

- **Count documents that match a specific condition**:
  ```bash
  db.collection_name.countDocuments({ field: "value" })
  ```

### Sorting and Limiting Results

- **Sort documents by a field (ascending order)**:

  ```bash
  db.collection_name.find().sort({ field: 1 })   # 1 for ascending, -1 for descending
  ```

- **Limit the number of results**:

  ```bash
  db.collection_name.find().limit(5)
  ```

- **Skip the first few documents**:
  ```bash
  db.collection_name.find().skip(5)
  ```

### Indexing

- **Create an index on a field**:

  ```bash
  db.collection_name.createIndex({ field: 1 })  # 1 for ascending index, -1 for descending
  ```

- **Show indexes of a collection**:

  ```bash
  db.collection_name.getIndexes()
  ```

- **Drop an index**:
  ```bash
  db.collection_name.dropIndex("index_name")
  ```

## Backup and Restore

### Backup a database:

```bash
mongodump --db database_name --out /path/to/backup/
```
