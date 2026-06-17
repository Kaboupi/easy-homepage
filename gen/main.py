from pathlib import Path

from utils import render_templates, Settings

BASE_DIR = Path(__file__).resolve().parent.parent

raw_config_dir = BASE_DIR / Settings.TEMPLATE_DIR / Settings.CONFIG_DIR
out_config_dir = BASE_DIR / Settings.RENDERED_DIR / Settings.CONFIG_DIR

raw_monitoring_dir = BASE_DIR / Settings.TEMPLATE_DIR / Settings.MONITORING_DIR
out_monitoring_dir = BASE_DIR / Settings.RENDERED_DIR / Settings.MONITORING_DIR


if __name__ == "__main__":
    render_templates(raw_dir=raw_config_dir, out_dir=out_config_dir)
    render_templates(raw_dir=raw_monitoring_dir, out_dir=out_monitoring_dir)
