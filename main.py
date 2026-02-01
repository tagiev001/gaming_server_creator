import docker


def build_image(tag: str, path: str):
    client = None
    try:
        client = docker.from_env()
        image, logs = client.images.build(path=path, tag=tag, rm=True)
        return image.tags[0]

    except docker.errors.BuildError as err:
        return f"Build error: {str(err)}"
    
    except docker.errors.APIError as err:
        return f"API error: {str(err)}"
    
    except Exception as err:
        return f"some error: {str(err)}"
    
    finally:
        if client:
            client.close()
        

def locate_dockerfiles(search_path: str)
    pass


def run_container()
    pass


def add_info_about_container()
    pass


def remove_info_about_container()
    pass


def stop_container()
    pass


def make_backup()
    pass


print(build_image("test:v1.1", "."))
