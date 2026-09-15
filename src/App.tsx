import { NavBar } from './components/NavBar';
import { useRouter } from './hooks/useRouter';
import { AboutPage } from './pages/AboutPage';
import { CalculatorPage } from './pages/CalculatorPage';
import { HomePage } from './pages/HomePage';
import { LibraryPage } from './pages/LibraryPage';
import './App.css';

function App() {
  const { route, navigate } = useRouter();

  return (
    <>
      <NavBar route={route} navigate={navigate} />
      <main>
        {route === 'home' && <HomePage navigate={navigate} />}
        {route === 'calculator' && <CalculatorPage />}
        {route === 'library' && <LibraryPage />}
        {route === 'about' && <AboutPage />}
      </main>
      <footer className="site-footer">
        <p>Educational tool — verify results independently before relying on them for real engineering work.</p>
      </footer>
    </>
  );
}

export default App;
