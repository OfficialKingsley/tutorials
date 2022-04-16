<!-- @format -->

# Introduction to apis

The term <abbr title="Application Programming Index">api</abbr> stands for Application programming index. It provides a way of serving some data.

## RESTful API

---

The REST in REST API stands for _Representational State Transfer_

The basic idea behind this is that we can transfer data, it can be as an alternative to the traditional webpage as we do not have to transfer html pages from our server but data usually in json format or

## Scenario

---

Let's say, we are the client and for example, we visit a webpage. A response is made to the server and for a traditional webpage, this response is an html document.

If you are using a SPA (Single Page Application) you send a request to the server once and you get just one html page which is then rerendered by the application dynamically with javascript

What if you need some data but not an html page for example like a mobile app. Instead of sending back html pages, it usually returns data in some data form like json

A restful api is just a server that serves data but usually doesn't serve html but serves another format of data lke json

## Things to note

---

Restful apis are stateless i.e. they do not depend on the type of client connected to it
<br />

##

---

Get post delete and patch

## What type of data

---

Data with a rest api could be transferred in many forms like json,cml, URLEncoded, formData but predominantly json

## Theory of a restful api

---

The above is theoretically just an api to show the specifications of a restful api, the following should be taken note of!

- Client - Server Architecture
  - Separation of concerns
  - The api shouldn't care about the UI of your app
- Stateless
  - No client data like sessions should be stored
  - APIs shouldn't care about the clients connecting to it
  - No matter the client, it should serve the data
- Cacheability
  - Data from your api should show themselves as cacheable or non-cacheable
  - For a rest api you should be made such that when a get request is made, you can specify whether the data can be cached and for how long
  - You can also specify the data shouldn't be cacheable at all
- Layered System
  - You could connect your own server to another server without your client even knowing
- Uniform Interface
  - Each url should point to a particular resource
  - Each data should be decoupled from a database into a different form
  - Self descriptive messages showing links to further resources about your works and apis
- Code on demand (Optional)
  - You can also send executable code from your api
