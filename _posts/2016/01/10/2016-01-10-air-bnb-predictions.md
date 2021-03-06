---
author: Elijah Bernstein-Cooper
category:
- hidden
comments: true
date: 2016-01-10 00:00
hidden: true
layout: post
redirect_from: /hidden/2016/01/10/air-bnb-predictions
tags:
- Kaggle
- Air-B&B
title: Predicting Air B&B User Travel
use_math: true
---

**Table of Contents**

<hr style="height:2px; background-color:#b6b6b6"/>

* TOC
{:toc}

<hr style="height:2px; background-color:#b6b6b6"/>

# Competition Description

I decided to have a go at the Kaggle competition for [predicting Air B&B user's
future travel](https://www.kaggle.com/c/airbnb-recruiting-new-user-bookings).


# The Data

The data description can be found
[here](https://www.kaggle.com/c/airbnb-recruiting-new-user-bookings/data). Below
is a description in my own words.

It may be beneficial later to combine the test data and the training data, then
randomly create a train, test, and validation dataset from the total sample.

## Training Data

  train_users.csv - the training set of users

## The Sample Data

The sample data consists of three segmented data sets

### Test Data

test_users.csv - the test set of users

+ id: user id
+ date_account_created: the date of account creation
+ timestamp_first_active: timestamp of the first activity, note that it can be earlier than date_account_created or date_first_booking because a user can search before signing up
+ date_first_booking: date of first booking
+ gender
+ age
+ signup_method
+ signup_flow: the page a user came to signup up from
+ language: international language preference
+ affiliate_channel: what kind of paid marketing
+ affiliate_provider: where the marketing is e.g. google, craigslist, other
+ first_affiliate_tracked: whats the first marketing the user interacted with before the signing up
+ signup_app
+ first_device_type
+ first_browser
+ country_destination: this is the target variable you are to predict

### User Data

+ sessions.csv - web sessions log for users
  + user_id: to be joined with the column 'id' in users table
  + action
  + action_type
  + action_detail
  + device_type
  + secs_elapsed

### Population Data

+ age_gender_bkts.csv - summary statistics of users' age group, gender, country 
                        of destination

### Country Data

+ countries.csv - summary statistics of destination countries in this dataset
                  and their locations


# First Examination of the Data

# Predictions of the Data

We should convert the labels into dummy variables and individually predict for
each country. Then join the results together.