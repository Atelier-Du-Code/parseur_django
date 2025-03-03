DO $$ 
BEGIN 
    CREATE ROLE utilisateur WITH LOGIN PASSWORD 'mdp_utilisateur';
    EXCEPTION WHEN duplicate_object THEN 
        NULL;
END $$;

ALTER ROLE utilisateur WITH SUPERUSER;
