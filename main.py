import docker




def build_image(tag: str, dockerfile: str,):
    client = None
    try:
        client = docker.from_env()
        image, logs = client.images.build(dockerfile=dockerfile, tag=tag, rm=True)
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
        

def locate_dockerfiles(search_path: str):
    pass


def run_gaming_server(game, ports, IPv4, ram, rom, game_files_path):
    pass


def add_info_about_container():
    pass


def remove_info_about_container():
    pass


def stop_container():
    pass


def make_backup():
    pass



SUPPORTED_GAMES = ['Minecraft', 'Terraria', 'Project Zomboid', 'Factorio']

print(build_image(SUPPORTED_GAMES[0], "mc/Dockerfilemc"))
