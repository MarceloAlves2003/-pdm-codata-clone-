from dagster import Definitions

from dagster_pdm.assets import atualizar_indicadores_frota


definitions = Definitions(assets=[atualizar_indicadores_frota])
