# Databricks notebook source
# MAGIC %sql
# MAGIC select * from main.lego.sets
# MAGIC sort by num_parts
# MAGIC limit 10;
