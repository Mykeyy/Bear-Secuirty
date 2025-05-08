{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { nixpkgs, flake-utils, ... }:
    flake-utils.lib.eachDefaultSystem (system:
      with import nixpkgs { inherit system; }; {
        devShells.default = mkShell {
          buildInputs = [
            (python312.withPackages (p:
              with p; [
                discordpy
                python-dotenv
                pytest
                aiohttp
                aiofiles
                cryptography
              ]))
            black
            lightning-loop
            ruff
            basedpyright
            pyright
          ];
        };
        formatter = nixfmt-tree;
      });
}