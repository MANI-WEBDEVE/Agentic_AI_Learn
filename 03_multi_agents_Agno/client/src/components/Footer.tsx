import React from 'react';

const Footer: React.FC = () => {
    return (
        <footer className="w-full bg-primary py-4 px-6 flex items-center justify-between fixed bottom-0 mb-10">
            <p className='text-center text-secondary text-sm text-white '>Developed By MANI-WEBEVE</p>
            <p className="text-center text-secondary text-sm text-white ">
                &copy; {new Date().getFullYear()} Financial Agent. All rights reserved.
            </p>
        </footer>
    );
};

export default Footer;
