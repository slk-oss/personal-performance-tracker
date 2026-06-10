from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):

      # 2. Перечисляем наши переменные и указываем их типы
      POSTGRES_USER: str      
      POSTGRES_PASSWORD: str 
      POSTGRES_DB: str        
      POSTGRES_PORT: int     
      SECRET_KEY: str         

      # 3. Настраиваем класс: говорим ему искать файл с именем ".env"
      model_config = SettingsConfigDict(env_file="../.env")

# 4. Создаем ОДИН готовый объект (экземпляр) этого класса.
settings = Settings()