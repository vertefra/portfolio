--
-- PostgreSQL database dump
--

-- Dumped from database version 12.4 (Ubuntu 12.4-0ubuntu0.20.04.1)
-- Dumped by pg_dump version 12.4 (Ubuntu 12.4-0ubuntu0.20.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: project; Type: TABLE; Schema: public; Owner: verte
--



ALTER TABLE public.project OWNER TO verte;

--
-- Name: project_id_seq; Type: SEQUENCE; Schema: public; Owner: verte
--

CREATE SEQUENCE public.project_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.project_id_seq OWNER TO verte;

--
-- Name: project_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: verte
--

ALTER SEQUENCE public.project_id_seq OWNED BY public.project.id;


--
-- Name: project id; Type: DEFAULT; Schema: public; Owner: verte
--

ALTER TABLE ONLY public.project ALTER COLUMN id SET DEFAULT nextval('public.project_id_seq'::regclass);


--
-- Data for Name: project; Type: TABLE DATA; Schema: public; Owner: verte
--

COPY public.project (id, title, description, tags, img_url, github, live) FROM stdin;
1	Tecky	Group project. Server written with express, handling relational Mongo database (one to one, many to many and one to many) and nested routes. Handle the request to google API to find geographic coordinates for locations. Front end written with ReactJS. Uses geolocation, conditional rendering and full jwt Authentication	JavaScript, ReactJS, Google API, MongoDb, NodeJS, JavaScript, HTML5, CSS3	/static/img/projects/tecky.png	https://github.com/vertefra/techJournalClient	https://techjournalclient.herokuapp.com/dashboard
2	Portfolio	This very website has a python flaskAPI server rendering dynamic jinja2 templates, the same templating engine used by the most popular python framework, Django. The front end requests are handled by JavaScript(ES6), database storing all the info is postgreSQL. Behind the scene a very intuitive "admin" interface allowed to insert, delete or modify all the projects and other info in the website.   	Python, fastAPI, PostgreSQL, JavaScript, CSS3, HTML5	/static/img/projects/portfolio.png	https://github.com/vertefra/portfolio	www.vertefra.com
3	Go Fiber API server	API server written in GO and Fiber, one of the fastest web framework currently available. It's connected with a MongoDB where stores data related to the user (one to many relation) and supports full CRUD and jwt authentication. \n\n	Go, Fiber, jwt, MongoDb, relationalDB, RESTAPI	/static/img/projects/go_server.png	https://github.com/vertefra/Go-fiber-todo/tree/master/Go-fiber-todo-api	https://go-vue-backend.herokuapp.com/
4	Parliamo	** Under Maintenance!! ** \nParliamo is a web-chat that uses a microservices backend architecture. A Python Service, using socketIO and fastAPI, is in charge of sending messages and real time events between users. Another Python service is in charge of authentication. A NodeJS/Express query services takes care of storing all the messages history in MongoDB database. All the events are orchestrated by a central event-bus that avoid direct communication between the services and stores all the events in a database. Front end written in ReactJS.   	Microservices, Python, SocketIO, NodeJS, Express, MongoDB, JavaScript, ReactJS, PostrgreSQL	/static/img/projects/parliamo.png	https://github.com/vertefra/parliamo-client	
\.


--
-- Name: project_id_seq; Type: SEQUENCE SET; Schema: public; Owner: verte
--

SELECT pg_catalog.setval('public.project_id_seq', 4, true);


--
-- Name: project project_pkey; Type: CONSTRAINT; Schema: public; Owner: verte
--

ALTER TABLE ONLY public.project
    ADD CONSTRAINT project_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

