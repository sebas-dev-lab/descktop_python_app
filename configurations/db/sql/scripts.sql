-- reverse Database --
create database ding_conn;


-- servers table --
CREATE TABLE IF NOT EXISTS public.servers (
	ip varchar(20) NOT NULL,
	username varchar(50) NOT NULL,
	with_ssh bool NULL,
	with_key bool NULL,
	with_password bool NULL,
	"password" varchar(100) NULL,
	path_key varchar(500) NULL,
	ssh_port int4 NULL,
	local_port int4 NOT NULL,
	remote_port int4 NOT NULL,
	id varchar(36) NOT NULL,
	created_at timestamp NULL,
	updated_at timestamp NULL,
	deleted_at timestamp NULL,
	is_deleted bool NULL,
	CONSTRAINT servers_pkey PRIMARY KEY (id)
);