# HTTP

Hyper text transfer Protocal is one of, if not the most, common ways of transfering information accross the web. What this system of information transfer does is it takes data in a machine friendly data format and transfers it accross the web. There are two parts to HTTP: the request, and the response. Part of the populatirty of HTTP is the guaranteed response to your requests.

### HTTP Request
All HTTP requests have 5 parts to them:
1. HTTP version
2. URL
    - the URL is an important part of the HTP Request, and each part of the URL plays a role.
    - http://www.localhost:5000/greeting?hostile=false
        - http: this part of the URL indicates what kind of request I am making.
        - www.localhost: this here is the **domain** name
        - 5000: is the **port** where the requests is going to be sent: the computer that is hosting the web server that recieves the http request is going to be "listening" on that particular port for our requests
        - /greeting: this is **path** of my request, these can contain one or more words, seperated by / and they can also contain what is called **path parameters**
        - ?hostile=false: these are our **query** parameters, which are normally used when you want to filter data
3. Verb 
    - the Verb of your HTTP requests provides context about what you are trying to accoomplish with you HTTP request. There are a few common Verbs that you will be
    working with.
        - GET (usually handled to receiving information)
        - PUT
        - POST
        - PATCH
        - DELETE
4. Headers
    - headers provide meta data about your HTTP request, and they can sometimes be useful when parsing information from your request

5. Body
    - the body of a request holds all the information for the request. This can be user in put data, it can be dates, whatever information you need to pass from the user in your web application is stored in the body of your request
        - GET requests may not have a body


### HTTP Response
1. HTTP Version
2. Headers
3. Body
    - this is where any pertinent information for the user is stored
4. Status Code
    - this is a quick indication of how the request was handled
    - 100 this is usually just meta data / general information
    - 200 this is success level
    - 300 this is the reroute level
    - 400 this is the failure level
        - specifically this is a requester failure
        - this could mean they sent the wrong data, or they made an HTTP request to the wrong location, etc.
    - 500 this is the failure level for the web server
        - this is not a failure of the requester, but a failure of the developer
    

### JSON
JavaScript Object Notation is the most common way that data is transferd accross the web. Essentiall, JSONs are formatted strings that work in key:value pairs. JSONs support 3 different data types: strings, numbers, and booleans. The reason JSONs are so popular is because they are easy for just about every programming language to parse.
"""json
{
    "name": "Eric Suminski",
    "profession": "Trainer",
    "Fun Fact": "I can't touch my left shnoulder with my left hand"
}
"""