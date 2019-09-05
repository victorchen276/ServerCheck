import click
import psutil
import json
import sys
import os
from ServerCheck.http_request import ping_servers

# @click.group()
# def cli():
#     pass
#
#
# @click.command(name="check", help="check whatever")
# def check():
#     print("hello workd")
#
#
# # Add the command as a subcommand of the cli group
# cli.add_command(check)
os.environ["DEBUG"] = "1"

@click.command(help="Check server connectivity in our dear network")
@click.option("--filename", "-f", default=None)
@click.option("--server", "-s", default=None, multiple=True)
def cli(filename, server):

  if not filename and not server:
      raise click.UsageError("must provide a JSON file or servers")

  # Create a set to prevent duplicate server/port combinations
  servers = set()

  # If --filename or -f option is used then attempt to read
  # the file and add all values to the `servers` set.
  if filename:
      try:
          with open(filename) as f:
              json_servers = json.load(f)
              for s in json_servers:
                  servers.add(s)
      except:
          print("Error: Unable to open or read JSON file")
          sys.exit(1)

  # If --server or -s option are used then add those values
  # to the set.
  if server:
      for s in server:
          servers.add(s)

  # Make requests and collect results
  results = ping_servers(servers)
  print("SuccessfulConnections ")
  print("--------------------- ")
  for server in results['success']:
      print(server)

  print("\nFailedConnections ")
  print("------------------ ")
  for server in results['failure']:
      print(server)