// Modern Navbar Component
import { useState } from 'react';

const Header = () => {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <nav className="flex w-full items-center justify-between px-8 py-4 backdrop-blur  ">
      <div className="text-2xl font-bold text-white cursor-pointer transition-colors hover:text-blue-400">
        Financial Agent
      </div>
      
      <div className="hidden md:flex items-center gap-8">
       
        <button className="rounded-full bg-blue-600 px-6 py-2 font-medium text-white transition-all hover:bg-blue-700 hover:-translate-y-0.5">
          Get Started
        </button>
      </div>

      <div className="md:hidden cursor-pointer" onClick={() => setIsOpen(!isOpen)}>
        <div className="h-[3px] w-[25px] bg-white my-[5px] transition-all"></div>
        <div className="h-[3px] w-[25px] bg-white my-[5px] transition-all"></div>
        <div className="h-[3px] w-[25px] bg-white my-[5px] transition-all"></div>
      </div>
    </nav>
  );
};

export default Header;
