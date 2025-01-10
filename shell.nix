# Pinned nix-stable commit January 10, 2025
let
	pkgs = import (fetchTarball "https://github.com/NixOS/nixpkgs/archive/3f0a8ac25fb674611b98089ca3a5dd6480175751.tar.gz") {};
in pkgs.mkShell {
	packages = [
   		(pkgs.python3.withPackages (python-pkgs: with python-pkgs; [
      			# select Python packages here
      			pandas
      			requests
				numpy
				pymongo
				matplotlib
				jupyterlab
				gspread
				sqlalchemy
				pyodbc
				gspread
    		]))
  	];
}
