# Databricks notebook source
DROP TABLE IF EXISTS diamonds;


CREATE TABLE diamonds
  USING csv
  OPTIONS (path "/databricks-datasets/Rdatasets/data-001/csv/ggplot2/diamonds01.csv", header "false")