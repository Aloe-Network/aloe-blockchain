from setuptools import setup

dependencies = [
    "blspy==1.0.2",  # Signature library
    "aloevdf==1.0.2",  # timelord and vdf verification
    "aloebip158==1.0",  # bip158-style wallet filters
    "aloepos==1.0.3",  # proof of space
    "clvm==0.9.6",
    "clvm_rs==0.1.7",
    "clvm_tools==0.4.3",
    "aiohttp==3.7.4",  # HTTP server for full node rpc
    "aiosqlite==0.17.0",  # asyncio wrapper for sqlite, to store blocks
    "bitstring==3.1.7",  # Binary data management library
    "colorlog==5.0.1",  # Adds color to logs
    "concurrent-log-handler==0.9.19",  # Concurrently log and rotate logs
    "cryptography==3.4.7",  # Python cryptography library for TLS - keyring conflict
    "keyring==23.0.1",  # Store keys in MacOS Keychain, Windows Credential Locker
    "keyrings.cryptfile==1.3.4",  # Secure storage for keys on Linux (Will be replaced)
    #  "keyrings.cryptfile==1.3.8",  # Secure storage for keys on Linux (Will be replaced)
    #  See https://github.com/frispete/keyrings.cryptfile/issues/15
    "PyYAML==5.4.1",  # Used for config file format
    "setproctitle==1.2.2",  # Gives the aloe processes readable names
    "sortedcontainers==2.3.0",  # For maintaining sorted mempools
    "websockets==8.1.0",  # For use in wallet RPC and electron UI
    "click==7.1.2",  # For the CLI
    "dnspython==2.1.0",  # Query DNS seeds
]

upnp_dependencies = [
    "miniupnpc==2.1",  # Allows users to open ports on their router
]

dev_dependencies = [
    "pytest",
    "pytest-asyncio",
    "flake8",
    "mypy",
    "black",
    "aiohttp_cors",  # For blackd
    "ipython",  # For asyncio debugging
]

kwargs = dict(
    name="aloe-blockchain",
    author="Mariano Sorgente",
    author_email="mariano@aloe.net",
    description="Aloe blockchain full node, farmer, timelord, and wallet.",
    url="https://aloe.net/",
    license="Apache License",
    python_requires=">=3.7, <4",
    keywords="aloe blockchain node",
    install_requires=dependencies,
    setup_requires=["setuptools_scm"],
    extras_require=dict(
        uvloop=["uvloop"],
        dev=dev_dependencies,
        upnp=upnp_dependencies,
    ),
    packages=[
        "build_scripts",
        "aloe",
        "aloe.cmds",
        "aloe.consensus",
        "aloe.daemon",
        "aloe.full_node",
        "aloe.timelord",
        "aloe.farmer",
        "aloe.harvester",
        "aloe.introducer",
        "aloe.plotting",
        "aloe.protocols",
        "aloe.rpc",
        "aloe.server",
        "aloe.simulator",
        "aloe.types.blockchain_format",
        "aloe.types",
        "aloe.util",
        "aloe.wallet",
        "aloe.wallet.puzzles",
        "aloe.wallet.rl_wallet",
        "aloe.wallet.cc_wallet",
        "aloe.wallet.did_wallet",
        "aloe.wallet.settings",
        "aloe.wallet.trading",
        "aloe.wallet.util",
        "aloe.ssl",
        "mozilla-ca",
    ],
    entry_points={
        "console_scripts": [
            "aloe = aloe.cmds.aloe:main",
            "aloe_wallet = aloe.server.start_wallet:main",
            "aloe_full_node = aloe.server.start_full_node:main",
            "aloe_harvester = aloe.server.start_harvester:main",
            "aloe_farmer = aloe.server.start_farmer:main",
            "aloe_introducer = aloe.server.start_introducer:main",
            "aloe_timelord = aloe.server.start_timelord:main",
            "aloe_timelord_launcher = aloe.timelord.timelord_launcher:main",
            "aloe_full_node_simulator = aloe.simulator.start_simulator:main",
        ]
    },
    package_data={
        "aloe": ["pyinstaller.spec"],
        "aloe.wallet.puzzles": ["*.clvm", "*.clvm.hex"],
        "aloe.util": ["initial-*.yaml", "english.txt"],
        "aloe.ssl": ["aloe_ca.crt", "aloe_ca.key", "dst_root_ca.pem"],
        "mozilla-ca": ["cacert.pem"],
    },
    use_scm_version={"fallback_version": "unknown-no-.git-directory"},
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    zip_safe=False,
)


if __name__ == "__main__":
    setup(**kwargs)
