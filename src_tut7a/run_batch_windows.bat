for /l %%i in (1, 1, 4) do (
   python main.py -c data/config_cp_inst%%i.yaml
)
