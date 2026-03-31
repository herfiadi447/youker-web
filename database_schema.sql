-- Supabase SQL Schema for Youker Web Solutions Contact Form

CREATE TABLE contacts (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    service VARCHAR(100),
    message TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Enable Row Level Security
ALTER TABLE contacts ENABLE ROW LEVEL SECURITY;

-- Create policy to allow public inserts (since it's a public contact form)
CREATE POLICY "Allow public insert on contacts" 
ON contacts FOR INSERT 
WITH CHECK (true);

-- Create policy to allow authenticated users to read (assuming admin later)
CREATE POLICY "Allow authenticated read on contacts" 
ON contacts FOR SELECT 
TO authenticated 
USING (true);
