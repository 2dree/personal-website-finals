import { createClient } from '@supabase/supabase-js';

const supabaseUrl = "https://glvqdlzsvdmvplohpmgq.supabase.co";
const supabaseKey = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImdsdnFkbHpzdmRtdnBsb2hwbWdxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDExNjAxNTYsImV4cCI6MjA1NjczNjE1Nn0.UauGe2SIarphoWwwAHweqDdV13wkK1k1lSgfFSjW0lc";

export const supabase = createClient(supabaseUrl, supabaseKey);
